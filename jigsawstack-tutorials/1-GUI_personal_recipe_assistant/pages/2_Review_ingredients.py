import streamlit as st
from jigsawstack import JigsawStack, JigsawStackError
from io import BytesIO
from PIL import Image, ImageOps

# Set Streamlit page configuration
st.set_page_config(
    page_title="Personal Recipe Assistant – Review Ingredients",
    menu_items={
        "Report a bug": "https://github.com/rokbenko/ai-playground",
    },
)

# Add custom CSS
st.markdown(
    """
        <style>
            button:hover {
                transition: 0.2s all ease-in-out;
            }
        </style>
    """,
    unsafe_allow_html=True,
)

# Retrieve JigsawStack API keys from secrets or get them from user inputs in the sidebar
if "JIGSAWSTACK_PRIVATE_API_KEY" in st.secrets:
    private_api_key = st.secrets["JIGSAWSTACK_PRIVATE_API_KEY"]
else:
    private_api_key = st.sidebar.text_input(
        label="#### Set your JigsawStack private(!) API key 👇",
        placeholder="sk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        type="password",
    )

if "JIGSAWSTACK_PUBLIC_API_KEY" in st.secrets:
    public_api_key = st.secrets["JIGSAWSTACK_PUBLIC_API_KEY"]
else:
    public_api_key = st.sidebar.text_input(
        label="#### Set your JigsawStack public(!) API key 👇",
        placeholder="pk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        type="default",
    )

# Initialize JigsawStack client with the API key
client = JigsawStack(api_key=private_api_key)


# Define a function for the user to review ingredients and switch to the next page
def main():
    """
    The main function of the application, responsible for displaying user interface,
    allowing users to review the recognized ingredients, edit, add, or remove ingredients,
    and navigating to the next page.

    This function performs the following tasks:
    1. Displays the title and subtitle of the page.
    2. Checks if a vOCR response is stored in the session state:
        - If not, it prompts the user to go back to the previous page and upload a photo.
        - If yes, it displays the recognized ingredients, allows the user to edit them and proceed to the next page.
    3. Displays a text area where the user can review, edit, add, or remove recognized ingredients.
    4. Displays the photo alongside the text area for reference.
    5. Provides a button to continue to the next page, storing any edits made by the user in the session state.
    6. Offers an optional dialog to show the data details of the recognized ingredients.
    7. Displays a "Powered by JigsawStack" badge.

    Parameters:
        None

    Returns:
        None
    """

    # Display page title
    st.markdown(
        "<h2 style='text-align: center;'>Review your ingredients! 🧐</h2>",
        unsafe_allow_html=True,
    )

    # Display page subtitle
    st.markdown(
        "<h5 style='text-align: center; margin-bottom: 1rem;'>Make sure everything is correct before we start cooking.</h5>",
        unsafe_allow_html=True,
    )

    # If vOCR response is not stored in session state
    if "vocr_response" not in st.session_state:
        # Initialize columns
        col_left, col_right = st.columns([0.8, 0.2])

        with col_left:
            # Display warning message
            st.warning(
                body="No photo has been uploaded yet. Please go back and upload a photo.",
                icon="⚠️",
            )
        with col_right:
            # Display previous page button
            previous_page_button = st.button(
                label="Go back", use_container_width=True, type="primary"
            )

        # If previous page button is clicked, switch pages
        if previous_page_button:
            st.switch_page("1_Upload_photo.py")

    # If vOCR response is stored in session state
    if "vocr_response" in st.session_state:
        # Display instructions
        st.markdown(
            "<p style='width: 75%; text-align: center; margin: auto; margin-bottom: 1rem;'>Feel free to edit, add, or remove any recognized ingredients in the text area below, using the photo as a reference.</p>",
            unsafe_allow_html=True,
        )

        # Get data from session state
        vocr_response_from_session_state = st.session_state["vocr_response"]

        # Extract ingredients
        ingredients = [
            ingredient.strip().capitalize()
            for ingredient in vocr_response_from_session_state["context"].split(",")
        ]

        # Initialize empty dictionary
        ingredients_dict = {}

        # Iterate through ingredients to build a dictionary that maps each ingredient's name to its bounding box coordinates
        for section in vocr_response_from_session_state["sections"]:
            for line in section["lines"]:
                for chunk in line["chunks"]:
                    ingredient_name = chunk["text"]
                    ingredient_bounds = chunk["bounds"]

                    ingredients_dict[ingredient_name] = {
                        "top_left": ingredient_bounds["top_left"],
                        "top_right": ingredient_bounds["top_right"],
                        "bottom_right": ingredient_bounds["bottom_right"],
                        "bottom_left": ingredient_bounds["bottom_left"],
                    }

        # Retrieve photo from JigsawStack
        try:
            jigsawstack_retrieved_photo = client.store.get("fridge.jpg")
        except JigsawStackError as e:
            st.error(body=f"{e}", icon="❌")

        # Create in-memory byte stream
        image_stream = BytesIO(jigsawstack_retrieved_photo.content)

        # Convert byte stream into PIL Image
        image_stream = BytesIO(jigsawstack_retrieved_photo.content)
        image = Image.open(image_stream)

        # Correct orientation based on EXIF data
        transposed_image = ImageOps.exif_transpose(image)

        # Initialize columns
        col_left, col_right = st.columns(2)

        with col_left:
            # Display text area
            reviewed_ingredients = st.text_area(
                label="Feel free to edit, add, or remove any recognized ingredients in the text area below, using the photo on the right as a reference.",
                label_visibility="collapsed",
                value=("- " + "\n- ".join(ingredients)),
                height=400,  # 25rem
            )

            # Display next page button
            next_page_button = st.button(
                label="Continue 🚀", use_container_width=True, type="primary"
            )

            # If next page button is clicked and text area value is available, store reviewed ingredients in session state and switch pages
            if next_page_button and reviewed_ingredients:
                st.session_state["reviewed_ingredients"] = reviewed_ingredients

                st.switch_page("pages/3_Select_preferences.py")
        with col_right:
            # Display photo
            st.image(transposed_image)

        # Display info message
        st.info(
            body="Curious how the ingredients were recognized from your photo? Click the button below to open a popup with all the data details.",
            icon="ℹ️",
        )

        # Display a button that opens a dialog with data details
        @st.dialog("Data details")
        def data_details():
            """
            A dialog box that displays the details of the ingredients.

            This function is a callback for a dialog box that is triggered when the "Show the data details"
            button is clicked. It uses the Streamlit library to create a dialog box and displays the
            contents of the `ingredients_dict` dictionary using the `st.write` function.

            Parameters:
                None

            Returns:
                None
            """

            st.write(ingredients_dict)

        # Initialize columns
        col_left, col_middle, col_right = st.columns(3)

        with col_left:
            st.write("&nbsp;")
        with col_middle:
            # Opens dialog
            st.button(
                label="Show the data details",
                use_container_width=True,
                on_click=data_details,
            )
        with col_right:
            st.write("&nbsp;")

    # Display "Powered by JigsawStack" badge
    st.markdown(
        "<div style='text-align: center; margin-top: 2.5rem;'><a href='https://jigsawstack.com/?ref=powered-by' rel='follow'><img style='width: 144px;' src='https://jigsawstack.com/badge.svg' alt='Powered by JigsawStack. The One API for your next big thing.' /></a></div>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    # Run the main function
    main()

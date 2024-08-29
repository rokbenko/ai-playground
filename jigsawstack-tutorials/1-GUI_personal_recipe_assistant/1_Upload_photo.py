import streamlit as st
from jigsawstack import JigsawStack, JigsawStackError
import time

# Set Streamlit page configuration
st.set_page_config(
    page_title="Personal Recipe Assistant – Upload Photo",
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


# Define a function to format the time
def format_time(milliseconds):
    """
    Formats a given time in milliseconds into a human-readable format.

    Args:
        milliseconds (int): The time in milliseconds to be formatted.

    Returns:
        str: The formatted time as a string, using milliseconds, seconds, or minutes as the unit of time.
    """

    if milliseconds < 1000:
        return f"{int(milliseconds)} ms"
    elif milliseconds < 60000:
        return f"{int(milliseconds/1000)} s"
    else:
        return f"{int(milliseconds/60000)} min"


# Define a function for the user to upload a photo to JigsawStack, recognize ingredients using JigsawStack and switch to the next page
def main():
    """
    The main function of the application, responsible for displaying the user interface,
    handling user input, uploading a photo to JigsawStack, recognizing ingredients using
    JigsawStack, and navigating to the next page based on user actions.

    This function performs the following tasks:
    1. Displays the title and subtitle of the page.
    2. Checks if a vOCR response is stored in the session state:
        - If not, it prompts the user to upload a photo.
        - If yes, it displays a success message and allows the user to proceed to the next page.
    3. Uploads the photo to JigsawStack and utilizes JigsawStack for ingredient recognition.
    4. Stores the recognized ingredients in the session state.
    5. Displays options for the user to either upload another photo or proceed to the next page.
    6. Handles the navigation to the next page or resets the session state based on user actions.
    7. Displays a "Powered by JigsawStack" badge.

    Parameters:
        None

    Returns:
        None
    """

    # Display page title
    st.markdown(
        "<h2 style='text-align: center;'>What will we cook today? 👨‍🍳</h2>",
        unsafe_allow_html=True,
    )

    # Display page subtitle
    st.markdown(
        "<h5 style='text-align: center; margin-bottom: 1rem;'>Recipes based on what you have in your fridge.</h5>",
        unsafe_allow_html=True,
    )

    # If vOCR response is not stored in session state
    if "vocr_response" not in st.session_state:
        # Display form
        with st.form("user_input"):
            # Display file uploader
            uploaded_photo = st.file_uploader(
                label="Let me see what's in your fridge!",
                type=["jpg", "jpeg", "png", "tif", "tiff", "avif", "heif", "heic"],
                accept_multiple_files=False,
            )

            # Initialize columns
            col_left, col_middle, col_right = st.columns(3)

            with col_left:
                st.write("&nbsp;")
            with col_middle:
                # Display submit button
                submit_button = st.form_submit_button(
                    label="Upload photo",
                    use_container_width=True,
                )
            with col_right:
                st.write("&nbsp;")

            # If submit button is clicked and there is no uploaded photo, display error message
            if submit_button and not uploaded_photo:
                st.toast(
                    body="Photo not uploaded yet. Please upload a photo.",
                    icon="❌",
                )

            # If submit button is clicked and there is an uploaded photo, upload it to JigsawStack, recognize ingredients using JigsawStack and redirect to the next page
            if submit_button and uploaded_photo:
                # Initialize the timer
                start_time = time.time()

                # Display status banner
                with st.status(
                    label="Recognizing ingredients from the uploaded photo...",
                    expanded=True,
                ):
                    # Initialize columns
                    col_left, col_right = st.columns([0.9, 0.1])

                    # Step 1: Upload photo to JigsawStack
                    # Read uploaded photo as bytes
                    bytes_photo = uploaded_photo.read()

                    # Upload photo to JigsawStack
                    try:
                        jigsawstack_uploaded_photo = client.store.upload(
                            bytes_photo,
                            {"overwrite": True, "filename": "fridge.jpg"},
                        )
                    except JigsawStackError as e:
                        st.error(body=f"{e}", icon="❌")

                    # Get URL of uploaded photo
                    url_uploaded_photo = jigsawstack_uploaded_photo["url"]

                    # Display status message
                    step_1_time = int((time.time() - start_time) * 1000)

                    with col_left:
                        st.write(
                            f"Photo {uploaded_photo.name} uploaded to JigsawStack ✔️"
                        )
                    with col_right:
                        st.write(format_time(step_1_time))

                    # Step 2: Recognize ingredients from uploaded photo using JigsawStack
                    # Recognize ingredients from uploaded photo using JigsawStack
                    try:
                        vocr_response = client.vision.vocr(
                            {
                                "prompt": "Recognize all food ingredients in this photo. If you're not sure about an ingredient, just ignore it. Return response with the following format: ingredient1, ingredient2, ingredient3, etc.",
                                "url": f"{url_uploaded_photo}?x-api-key={public_api_key}",
                            }
                        )
                    except JigsawStackError as e:
                        st.error(body=f"{e}", icon="❌")

                    # If vOCR response is available and not stored in session state, store it in session state
                    if vocr_response and "vocr_response" not in st.session_state:
                        st.session_state["vocr_response"] = vocr_response

                    # Display status message
                    step_2_time = int((time.time() - start_time) * 1000)

                    with col_left:
                        st.write(
                            f"Photo {uploaded_photo.name} ingredients recognized using JigsawStack ✔️"
                        )
                    with col_right:
                        st.write(format_time(step_2_time))

    # If vOCR response is stored in session state
    if "vocr_response" in st.session_state:
        # Display success message
        st.success(
            body="Ingredients successfully recognized from the uploaded photo.",
            icon="✔️",
        )

        # Initialize columns
        col_left, col_right = st.columns(2)

        with col_left:
            # Display reset button
            reset_button = st.button(
                label="Upload another photo",
                use_container_width=True,
                type="secondary",
            )
        with col_right:
            # Display next page button
            next_page_button = st.button(
                label="Continue 🚀", use_container_width=True, type="primary"
            )

        # If reset button is clicked, reset vOCR response in session state and rerun the app
        if reset_button:
            del st.session_state["vocr_response"]
            st.rerun()

        # If next page button is clicked, switch pages
        if next_page_button:
            st.switch_page("pages/2_Review_ingredients.py")

    # Display "Powered by JigsawStack" badge
    st.markdown(
        "<div style='text-align: center;'><a href='https://jigsawstack.com/?ref=powered-by' rel='follow'><img style='width: 144px;' src='https://jigsawstack.com/badge.svg' alt='Powered by JigsawStack. The One API for your next big thing.' /></a></div>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    # Run the main function
    main()

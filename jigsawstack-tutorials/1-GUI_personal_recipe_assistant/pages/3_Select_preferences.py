import streamlit as st

# Set Streamlit page configuration
st.set_page_config(
    page_title="Personal Recipe Assistant – Select Preferences",
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


# Define a function for the user to select preferences and switch to the next page
def main():
    """
    The main function of the application, responsible for displaying user interface,
    allowing users to select their meal preferences, including meal types, cooking
    time, cuisines, dietary restrictions, and serving size, and navigating to the
    next page.

    This function performs the following tasks:
    1. Displays the title and subtitle of the page.
    2. Checks if a vOCR response and reviewed ingredients are stored in the session state:
        - If neither are stored, it prompts the user to go back and upload a photo.
        - If the vOCR response is stored but ingredients are not reviewed, it prompts the
          user to review ingredients.
        - If both are stored, it displays a form for users to select meal preferences.
    3. Provides widgets for selecting meal types, cooking time, cuisines, dietary restrictions,
       and serving size.
    4. Provides a button to continue to the next page, storing the selected meal preferences in the session state.
    5. Displays a "Powered by JigsawStack" badge.

    Parameters:
        None

    Returns:
        None
    """

    # Add page title
    st.markdown(
        "<h2 style='text-align: center;'>Select your preferences! 🍽️</h2>",
        unsafe_allow_html=True,
    )

    # Add page subtitle
    st.markdown(
        "<h5 style='text-align: center; margin-bottom: 1rem;'>Customize your meal to match your taste, time, and dietary needs.</h5>",
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

    # If vOCR response is stored in session state, but reviewed ingredients are not stored in session state
    if (
        "vocr_response" in st.session_state
        and "reviewed_ingredients" not in st.session_state
    ):
        # Initialize columns
        col_left, col_right = st.columns([0.8, 0.2])

        with col_left:
            # Display warning message
            st.warning(
                body="Ingredients have not been reviewed yet. Please go back and review ingredients.",
                icon="⚠️",
            )
        with col_right:
            # Display previous page button
            previous_page_button = st.button(
                label="Go back", use_container_width=True, type="primary"
            )

        # If previous page button is clicked, switch pages
        if previous_page_button:
            st.switch_page("pages/2_Review_ingredients.py")

    # If vOCR response and reviewed ingredients are stored in session state
    if (
        "vocr_response" in st.session_state
        and "reviewed_ingredients" in st.session_state
    ):
        # Initialize columns
        col_left, col_middle, col_right = st.columns([0.1, 0.8, 0.1])

        with col_left:
            st.write("&nbsp;")
        with col_middle:
            # Display form
            with st.form("user_preferences"):
                # Add select and multiselect widgets
                meal_types = st.multiselect(
                    label="Select meal types (multiple selections allowed)",
                    options=[
                        "Breakfast",
                        "Brunch",
                        "Lunch",
                        "Dinner",
                        "Snack",
                        "Dessert",
                    ],
                    default=None,
                )

                cooking_time = st.selectbox(
                    label="Select cooking time",
                    options=[
                        "Up to 15 minutes",
                        "Up to 30 minutes",
                        "Up to 45 minutes",
                        "Up to 60 minutes",
                        "Over 60 minutes",
                    ],
                    index=None,
                )

                cuisines = st.multiselect(
                    label="Select cuisines (multiple selections allowed)",
                    options=[
                        "African",
                        "American",
                        "Chinese",
                        "French",
                        "Greek",
                        "Indian",
                        "Italian",
                        "Japanese",
                        "Korean",
                        "Mediterranean",
                        "Mexican",
                        "Spanish",
                        "Thai",
                        "Vietnamese",
                    ],
                    default=None,
                )

                diets_allergies_intolerances = st.multiselect(
                    label="Select diets, allergies, or intolerances (multiple selections allowed)",
                    options=[
                        "Dairy-free",
                        "Eggs-free",
                        "Fish-free",
                        "Gluten-free",
                        "Lactose-free",
                        "Peanuts-free",
                        "Sesame-free",
                        "Shellfish-free",
                        "Soy-free",
                        "Vegan",
                        "Vegetarian",
                        "Wheat-free",
                    ],
                    default=None,
                )

                serving_size = st.selectbox(
                    label="Select serving size",
                    options=[
                        "1 serving",
                        "2 servings",
                        "Family (4-6 servings)",
                        "Party (8-12 servings)",
                    ],
                    index=None,
                )

                # Display submit button
                next_page_button = st.form_submit_button(
                    label="Continue 🚀",
                    use_container_width=True,
                )

                # Initialize empty dictionary
                preferences_dict = {}

                # If next page button is clicked, build preferences dictionary, store preferences in session state and switch pages
                if next_page_button:
                    # Build preferences dictionary
                    preferences_dict = {
                        "meal_types": meal_types,
                        "cooking_time": cooking_time,
                        "cuisines": cuisines,
                        "diets_allergies_intolerances": diets_allergies_intolerances,
                        "serving_size": serving_size,
                    }

                    st.session_state["preferences"] = preferences_dict

                    st.switch_page("pages/4_Get_recipes.py")
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

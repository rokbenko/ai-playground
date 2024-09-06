import streamlit as st
from jigsawstack import JigsawStack, JigsawStackError

# Set Streamlit page configuration
st.set_page_config(
    page_title="Personal Recipe Assistant – Get Recipes",
    menu_items={
        "Report a bug": "https://github.com/rokbenko/ai-playground",
    },
    layout="wide",
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


# Define a function to create the recipe prompt
def create_recipe_prompt():
    """
    Creates a personalized recipe prompt using the JigsawStack prompt engine.

    This function uses the JigsawStack prompt engine to create a recipe prompt tailored to the user's ingredients and preferences.

    The prompt is configured with the following parameters:
        - ingredients (list of str): A list of ingredients available for use in the recipe.
        - meal_types (list of str): Types of meals the user is interested in (e.g., breakfast, lunch, dinner).
        - cooking_time (str): The maximum amount of time (e.g., "30 minutes") the user is willing to spend cooking.
        - cuisines (list of str): Preferred cuisines (e.g., Italian, Chinese) to guide the recipe selection.
        - dietary_restrictions (list of str): Dietary restrictions (e.g., vegetarian, gluten-free) that the recipe must adhere to.
        - serving_size (int): The number of servings or people the recipe should accommodate.

    Three very different detailed recipes will be generated, each adhering to the specified preferences.

    If any required ingredients are missing from the user's provided list, they will be noted under a "Missing Ingredients" section for each recipe.

    The function returns a dictionary indicating the success of the prompt creation and includes the unique ID of the created prompt.

    Parameters:
        None

    Error Handling:
        - If the prompt generation process fails due to a JigsawStackError, an error message is displayed to the user.

    Returns:
        - dict: A dictionary containing the following keys:
            - success (bool): Indicates whether the prompt creation was successful.
            - prompt_engine_id (str): The unique identifier of the created prompt.

    Raises:
        - JigsawStackError: If an error occurs while generating the recipe prompt.
    """

    try:
        jigsawstack_create_recipe_prompt = client.prompt_engine.create(
            {
                "prompt": """
                    You are my personal recipe assistant. Your task is to generate 3 very different detailed recipes, based on my current preferences and available ingredients.

                    Please follow these guidelines when creating the recipe:
                    - Available ingredients: {ingredients}. You may include additional ingredients if necessary, but clearly list any missing ingredients required for the recipe.
                    - Meal types: {meal_types}. The recipe must fit the selected meal types.
                    - Cooking time: {cooking_time}. The recipe must be prepared within this time frame.
                    - Cuisines: {cuisines}. The recipe must align with the selected cuisines.
                    - Dietary restrictions: {dietary_restrictions}. The recipe must adhere to the selected dietary restrictions.
                    - Serving size: {serving_size}. The recipe must match the selected serving size.
                
                    All preferences and restrictions, except for the available ingredients, are non-negotiable. Clearly list any missing ingredients under a "Missing Ingredients" section for each recipe.
                """,
                "inputs": [
                    {
                        "key": "ingredients",
                        "optional": False,
                    },
                    {
                        "key": "meal_types",
                        "optional": True,
                    },
                    {
                        "key": "cooking_time",
                        "optional": True,
                    },
                    {
                        "key": "cuisines",
                        "optional": True,
                    },
                    {
                        "key": "dietary_restrictions",
                        "optional": True,
                    },
                    {
                        "key": "serving_size",
                        "optional": True,
                    },
                ],
                "return_prompt": "Return the result in a markdown format. Use H3 as the header of the recipe. Use H4 as the header for each recipe section. Separate each recipe with a divider.",
            }
        )

        return jigsawstack_create_recipe_prompt
    except JigsawStackError as e:
        st.error(body=f"{e}", icon="❌")


# Define a function to retrieve all prompts
def list_all_prompts():
    """
    Retrieves a list of all prompts available in the JigsawStack prompt engine.

    This function uses the JigsawStack prompt engine to fetch a list of all prompts.

    The function returns a dictionary containing detailed information about each prompt, such as its ID, text, input parameters, and other metadata.

    Parameters:
        None

    Error Handling:
        - If the prompt retrieval process fails due to a JigsawStackError, an error message is displayed to the user.

    Returns:
        - dict: A dictionary containing the following keys:
            - success (bool): Indicates whether the prompt retrieval was successful.
            - prompt_engines (list of dict): A list of dictionaries, each representing a prompt with the following details:
                - id (str): The unique identifier of the prompt.
                - prompt (str): The text of the prompt.
                - inputs (list of dict): A list of input parameters required by the prompt. Each input dictionary contains:
                    - key (str): The name of the input parameter.
                    - optional (bool): Whether the input parameter is optional.
                - return_prompt (str): The format in which the result should be returned.
                - return_prompt_type (str): The data type of the returned result.
                - created_at (str): The timestamp when the prompt was created.
            - page (int): The current page of the results.
            - limit (int): The maximum number of prompts returned per page.
            - has_more (bool): Indicates whether there are more prompts to be retrieved beyond the current page.

    Raises:
        - JigsawStackError: If an error occurs while fetching the list of all prompts.
    """

    try:
        jigsawstack_list_all_prompts = client.prompt_engine.list()

        return jigsawstack_list_all_prompts
    except JigsawStackError as e:
        st.error(body=f"{e}", icon="❌")


# Define a function to retrieve a prompt for a given ID
def get_prompt(id):
    """
    Retrieves a specific prompt available in the JigsawStack prompt engine using the provided ID.

    This function uses the JigsawStack prompt engine to fetch the detailed information about a prompt associated with the provided `id`.

    The function returns a dictionary containing detailed information about the prompt, such as its ID, text, input parameters, and other metadata.

    Parameters:
        - id (str): The unique identifier of the prompt to retrieve. This value must be a non-empty string.

    Error Handling:
        - If the `id` is an empty string, a toast notification is displayed asking the user to provide a valid prompt ID.
        - If the prompt retrieval process fails due to a JigsawStackError, an error message is displayed to the user.

    Returns:
        - dict: A dictionary containing the following keys:
            - success (bool): Indicates whether the prompt retrieval was successful.
            - id (str): The unique identifier of the retrieved prompt.
            - inputs (list of dict): A list of input parameters required by the prompt. Each input dictionary contains:
                - key (str): The name of the input parameter.
                - optional (bool): Whether the input parameter is optional.
            - prompt (str): The text of the prompt.
            - return_prompt (str): The format in which the result should be returned.
            - created_at (str): The timestamp when the prompt was created.
            - groq_key (NoneType): Currently `None`, reserved for future use or additional data.

    Raises:
        - JigsawStackError: If an error occurs while fetching the prompt.
    """

    if id == "":
        st.toast(body="Please enter a prompt ID", icon="❌")
    else:
        try:
            jigsawstack_get_prompt = client.prompt_engine.get(id)

            return jigsawstack_get_prompt
        except JigsawStackError as e:
            st.error(body=f"{e}", icon="❌")


# Define a function to delete a prompt for a given ID
def delete_prompt(id):
    """
    Deletes a specific prompt from the JigsawStack prompt engine using the provided ID.

    This function uses the JigsawStack prompt engine to remove a prompt associated with the provided `id`.

    The function returns a dictionary indicating the success of the prompt removal and includes the unique ID of the removed prompt.

    Parameters:
        - id (str): The unique identifier of the prompt to delete. This value must be a non-empty string.

    Error Handling:
        - If the `id` is an empty string, a toast notification is displayed asking the user to provide a valid prompt ID.
        - If the prompt deletion process fails due to a JigsawStackError, an error message is displayed to the user.

    Returns:
        - dict: A dictionary containing the following keys:
            - success (bool): Indicates whether the prompt removal was successful.
            - prompt_engine_id (str): The unique identifier of the removed prompt.

    Raises:
        - JigsawStackError: If an error occurs while deleting the recipe prompt.
    """

    if id == "":
        st.toast(body="Please enter a prompt ID", icon="❌")
    else:
        try:
            jigsawstack_delete_prompt = client.prompt_engine.delete(id)

            return jigsawstack_delete_prompt
        except JigsawStackError as e:
            st.error(body=f"{e}", icon="❌")


# Define a function to generate recipes
def generate_recipes():
    """
    Generates three recipes using the JigsawStack prompt engine by utilizing the created personalized recipe prompt.

    This function uses the JigsawStack prompt engine to utilize the created personalized recipe prompt (created with the `create_recipe_prompt` function) to generate three recipes tailored to the user's ingredients and preferences.

    This function performs the following tasks:
        1. Retrieves the recipe prompt ID, reviewed ingredients, and user preferences from the session state.
        2. Constructs an input dictionary that includes the ingredients and preferences if they are provided by the user.
        3. Calls the JigsawStack API with the constructed input dictionary to generate three recipes.
        4. Returns the generated three recipes or displays an error message if the API call fails.

    Parameters:
        None

    Error Handling:
        - If the recipe generation process fails due to a JigsawStackError, an error message is displayed to the user.

    Returns:
        - str: The generated three recipes.

    Raises:
        - JigsawStackError: If an error occurs while generating the three recipes.
    """

    # Retrieve recipe prompt ID, ingredients and preferences from session state
    recipe_prompt_id = st.session_state["recipe_prompt_id"]
    ingredients_from_session_state = st.session_state["reviewed_ingredients"]
    preferences_from_session_state = st.session_state["preferences"]

    # Initialize input dictionary
    input_values_dict = {}

    # Check and add each parameter only if it's not empty or None
    if ingredients_from_session_state:
        input_values_dict["ingredients"] = ingredients_from_session_state

    if preferences_from_session_state["meal_types"]:
        input_values_dict["meal_types"] = ", ".join(
            preferences_from_session_state["meal_types"]
        )

    if preferences_from_session_state["cooking_time"] is not None:
        input_values_dict["cooking_time"] = ", ".join(
            preferences_from_session_state["cooking_time"]
        )

    if preferences_from_session_state["cuisines"]:
        input_values_dict["cuisines"] = ", ".join(
            preferences_from_session_state["cuisines"]
        )

    if preferences_from_session_state["diets_allergies_intolerances"]:
        input_values_dict["diets_allergies_intolerances"] = ", ".join(
            preferences_from_session_state["diets_allergies_intolerances"]
        )

    if preferences_from_session_state["serving_size"] is not None:
        input_values_dict["serving_size"] = ", ".join(
            preferences_from_session_state["serving_size"]
        )

    try:
        jigsawstack_run_recipe_prompt = client.prompt_engine.run(
            {
                "id": recipe_prompt_id,
                "input_values": input_values_dict,
            }
        )

        return jigsawstack_run_recipe_prompt["result"]
    except JigsawStackError as e:
        st.error(body=f"{e}", icon="❌")


# Define a function for the user to generate recipes using JigsawStack
def main():
    """
    The main function of the application, responsible for displaying user interface,
    allowing users to generate recipes using JigsawStack based on the ingredients
    and preferences they have chosen.

    This function performs the following tasks:
        1. Displays the title and subtitle of the page.
        2. Handles the navigation between the 1st, 2nd, and 3rd pages as follows:
            - If the user has not uploaded a photo yet, it will display a warning message
            and a button to switch to the 1st page.
            - If the user has uploaded a photo but has not reviewed the ingredients yet,
            it will display a warning message and a button to switch to the 2nd page.
            - If the user has uploaded a photo and reviewed the ingredients but has not
            chosen preferences yet, it will display a warning message and a button to
            switch to the 3rd page.
        3. Handles the core functionality of the application as follows:
            - If the user has uploaded a photo, reviewed the ingredients and chosen
            preferences, it will generate recipes based on the ingredients and
            preferences chosen by the user and store them in session state.
        4. Displays a tab for managing prompts and a tab for generating
        recipes. The tab for managing prompts allows the user to create a prompt,
        list all prompts, get a prompt and delete a prompt. The tab for generating
        recipes allows the user to generate recipes based on the ingredients and
        preferences chosen by the user.
        5. Displays a "Powered by JigsawStack" badge.

    Parameters:
        None

    Returns:
        None
    """

    # Add page title
    st.markdown(
        "<h2 style='text-align: center;'>Bon Appétit! 🍲</h2>",
        unsafe_allow_html=True,
    )

    # Add page subtitle
    st.markdown(
        "<h5 style='text-align: center; margin-bottom: 1rem;'>Follow the steps below to create your delicious dish.</h5>",
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

    # If vOCR response and reviewed ingredients are stored in session state, but preferences are not stored in session state
    if (
        "vocr_response" in st.session_state
        and "reviewed_ingredients" in st.session_state
        and "preferences" not in st.session_state
    ):
        # Initialize columns
        col_left, col_right = st.columns([0.8, 0.2])

        with col_left:
            # Display warning message
            st.warning(
                body="Preferences not chosen yet. Please go back and choose preferences.",
                icon="⚠️",
            )
        with col_right:
            # Display previous page button
            previous_page_button = st.button(
                label="Go back", use_container_width=True, type="primary"
            )

        # If previous page button is clicked, switch pages
        if previous_page_button:
            st.switch_page("pages/3_Select_preferences.py")

    # If vOCR response, reviewed ingredients, and preferences are stored in session state
    if (
        "vocr_response" in st.session_state
        and "reviewed_ingredients" in st.session_state
        and "preferences" in st.session_state
    ):
        # Initialize tabs
        tab_prompts, tab_recipe = st.tabs(["Manage prompts", "Generate recipes"])

        # Body for tab "Manage prompts"
        with tab_prompts:
            # Initialize columns
            col_left, col_right = st.columns([0.4, 0.6])

            # IMPORTANT: Right column needs to be placed first in order for placeholder to work
            with col_right:
                right_column_placeholder = st.empty()
            with col_left:
                # Display subheading
                st.markdown("#### Create the recipe prompt")

                # Display button
                create_recipe_prompt_button = st.button(
                    label="Create the recipe prompt",
                    use_container_width=True,
                )

                # If button is clicked, run create_recipe_prompt() function, store prompt ID in session state and display output with success message in right column
                if create_recipe_prompt_button:
                    with right_column_placeholder.container():
                        with st.status(
                            label="Creating the recipe prompt...",
                            expanded=True,
                        ):
                            output = create_recipe_prompt()

                            st.session_state["recipe_prompt_id"] = output[
                                "prompt_engine_id"
                            ]

                            if output["success"] == True:
                                st.success(
                                    body="The recipe prompt has been created successfully. You can now switch to the 'Generate recipes' tab and generate recipes as many times as you want.",
                                    icon="✔️",
                                )

                            st.write(output)

                st.divider()

                # Display subheading
                st.markdown("#### List all prompts")

                # Display button
                list_all_prompts_button = st.button(
                    label="List all prompts",
                    use_container_width=True,
                )

                # If button is clicked, run list_all_prompts() function and display output with success message in right column
                if list_all_prompts_button:
                    with right_column_placeholder.container():
                        with st.status(
                            label="Listing all prompts...",
                            expanded=True,
                        ):
                            output = list_all_prompts()

                            if output["success"] == True:
                                st.success(
                                    body="The list of all prompts has been retrieved successfully.",
                                    icon="✔️",
                                )

                            st.write(output)

                st.divider()

                # Display subheading
                st.markdown("#### Get a prompt")

                # Display text input
                get_prompt_id = st.text_input(
                    label="Enter prompt ID 👇",
                    placeholder="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    type="default",
                    key="get_id_to_get_prompt",
                )

                # Display button
                get_prompt_button = st.button(
                    label="Get a prompt",
                    use_container_width=True,
                )

                # If button is clicked, run get_prompt() function and display output with success message in right column
                if get_prompt_button:
                    with right_column_placeholder.container():
                        with st.status(
                            label="Getting the prompt...",
                            expanded=True,
                        ):
                            output = get_prompt(get_prompt_id)

                            if output == None:
                                st.error(body="Please enter a prompt ID", icon="❌")
                            elif output["success"] == True:
                                st.success(
                                    body="The prompt has been retrieved successfully.",
                                    icon="✔️",
                                )

                                st.write(output)

                st.divider()

                # Display subheading
                st.markdown("#### Delete a prompt")

                # Display text input
                delete_prompt_id = st.text_input(
                    label="Enter prompt ID 👇",
                    placeholder="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    type="default",
                    key="get_id_to_delete_prompt",
                )

                # Display button
                delete_prompt_button = st.button(
                    label="Delete a prompt",
                    use_container_width=True,
                )

                # If button is clicked, run delete_prompt() function and display output with success message in right column
                if delete_prompt_button:
                    with right_column_placeholder.container():
                        with st.status(
                            label="Deleting the prompt...",
                            expanded=True,
                        ):
                            output = delete_prompt(delete_prompt_id)

                            if output == None:
                                st.error(body="Please enter a prompt ID", icon="❌")
                            elif output["success"] == True:
                                st.success(
                                    body="The prompt has been deleted successfully.",
                                    icon="✔️",
                                )

                                st.write(output)

        # Body for tab "Generate recipes"
        with tab_recipe:
            # If recipe prompt ID is not stored in session state, display warning message
            if "recipe_prompt_id" not in st.session_state:
                st.warning(
                    body="No recipe prompt has been created yet. Please switch to the 'Manage prompts' tab and create the recipe prompt.",
                    icon="⚠️",
                )

            # If recipe prompt ID is stored in session state, display ingredients and preferences and generate recipes
            if "recipe_prompt_id" in st.session_state:
                # Retrieve ingredients and preferences from session state
                ingredients_from_session_state = st.session_state[
                    "reviewed_ingredients"
                ]
                preferences_from_session_state = st.session_state["preferences"]

                # Initialize columns
                col_left, col_middle, col_right = st.columns([0.2, 0.25, 0.55])

                with col_left:
                    # Display ingredients
                    st.markdown("#### Ingredients")

                    st.write(ingredients_from_session_state)
                with col_middle:
                    # Display preferences
                    st.markdown("#### Preferences")

                    # If meal types are not empty in session state, display them
                    if preferences_from_session_state["meal_types"] != []:
                        items_str = ", ".join(
                            preferences_from_session_state["meal_types"]
                        )

                        st.markdown(
                            f"Meal types:\n- {items_str}",
                        )

                        st.divider()

                    # If cooking time is not None in session state, display it
                    if preferences_from_session_state["cooking_time"] is not None:
                        st.markdown(
                            f"Cooking time:\n- {preferences_from_session_state['cooking_time']}",
                        )

                        st.divider()

                    # If cuisines are not empty in session state, display them
                    if preferences_from_session_state["cuisines"] != []:
                        items_str = ", ".join(
                            preferences_from_session_state["cuisines"]
                        )

                        st.markdown(
                            f"Cuisines:\n- {items_str}",
                        )

                        st.divider()

                    # If diets, allergies and intolerances are not empty in session state, display them
                    if (
                        preferences_from_session_state["diets_allergies_intolerances"]
                        != []
                    ):
                        items_str = ", ".join(
                            preferences_from_session_state[
                                "diets_allergies_intolerances"
                            ]
                        )

                        st.markdown(
                            f"Diets, allergies and intolerances:\n- {items_str}",
                        )

                        st.divider()

                    # If serving size is not None in session state, display it
                    if preferences_from_session_state["serving_size"] is not None:
                        st.markdown(
                            f"Serving size:\n- {preferences_from_session_state['serving_size']}",
                        )
                with col_right:
                    # Display change ingredients button
                    change_ingredients_button = st.button(
                        label="Change ingredients",
                        use_container_width=True,
                        type="secondary",
                    )

                    # Display change preferences button
                    change_preferences_button = st.button(
                        label="Change preferences",
                        use_container_width=True,
                        type="secondary",
                    )

                    # Display generate recipes button
                    generate_recipes_button = st.button(
                        label="Generate recipes 🚀",
                        use_container_width=True,
                        type="primary",
                    )

                    # If change ingredients button is clicked, switch pages
                    if change_ingredients_button:
                        st.switch_page("pages/2_Review_ingredients.py")

                    # If change preferences button is clicked, switch pages
                    if change_preferences_button:
                        st.switch_page("pages/3_Select_preferences.py")

                    # If generate recipes button is clicked and recipe prompt ID is not stored in session state, display error message
                    if (
                        generate_recipes_button
                        and "recipe_prompt_id" not in st.session_state
                    ):
                        st.toast(
                            body="The recipe prompt has not been generated yet. Please switch to the 'Manage prompts' tab and generate the recipe prompt.",
                            icon="❌",
                        )

                    # If generate recipes button is clicked and recipe prompt ID is stored in session state, run generate_recipes() function, store recipes in session state and display output
                    if (
                        generate_recipes_button
                        and "recipe_prompt_id" in st.session_state
                    ):
                        # Display status banner
                        with st.status(
                            label="Generating 3 recipes...",
                            expanded=True,
                        ):
                            output = generate_recipes()

                            st.session_state["recipes"] = output

                            st.write(output)

    # Display "Powered by JigsawStack" badge
    st.markdown(
        "<div style='text-align: center; margin-top: 2.5rem;'><a href='https://jigsawstack.com/?ref=powered-by' rel='follow'><img style='width: 144px;' src='https://jigsawstack.com/badge.svg' alt='Powered by JigsawStack. The One API for your next big thing.' /></a></div>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    # Run the main function
    main()

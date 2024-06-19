import streamlit as st
from openai import OpenAI, OpenAIError

# Set Streamlit page configuration
st.set_page_config(
    page_title="Select an OpenAI assistant to chat with",
    menu_items={
        "Report a bug": "https://github.com/rokbenko/ai-playground",
    },
)

# Retrieve OpenAI API key from secrets or get it from user input in the sidebar
if "OPENAI_API_KEY" in st.secrets:
    my_api_key = st.secrets["OPENAI_API_KEY"]
else:
    my_api_key = st.sidebar.text_input(
        label="#### Set your OpenAI API key here 👇",
        placeholder="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        type="password",
    )

# Initialize OpenAI client with the API key
client = OpenAI(
    api_key=my_api_key,
)

# Initialize session state variables if they do not exist
if "thread" not in st.session_state:
    st.session_state["thread"] = None

if "assistant" not in st.session_state:
    st.session_state["assistant"] = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# Add page title
st.markdown(
    "<h2 style='text-align: center; margin-bottom: 1rem;'>Select an OpenAI assistant to chat with</h2>",
    unsafe_allow_html=True,
)

# Create layout columns
col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

# Display error message if API key is not set
if not my_api_key:
    with col2:
        st.error("Please set your OpenAI API key in the sidebar.", icon="⚠️")

else:
    # If API key is set, allow user to select an assistant and start chat
    with col2:
        # Selectbox to select an OpenAI assistant
        option = st.selectbox(
            label="Select an OpenAI assistant to chat with",
            options=(
                "Customer support chatbot (File Search tool)",
                "Personal math tutor (Code Interpreter tool)",
            ),
            placeholder="Select an OpenAI assistant",
        )

        # Button to start chat
        start_chat_btn = st.button("Start chat 🚀", use_container_width=True)

        # If button is clicked
        if start_chat_btn:
            # Store selected assistant in session state
            st.session_state["assistant"] = option

            try:
                # Create a new thread with the OpenAI client
                my_thread = client.beta.threads.create()

                # Store thread in session state
                st.session_state["thread"] = my_thread

            except OpenAIError as e:
                st.error(e, icon="⚠️")

            # Switch to the chat page
            st.switch_page("pages/2_Chat_with_the_selected_OpenAI_assistant.py")

        # Add footer with social media links
        st.markdown(
            """
                <div style='text-align: center; margin-top: 1.5rem;'>
                    <div style='margin-bottom: 0.5rem;'>Made with ❤️ by Rok Benko</div>
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
                    <a href="https://www.linkedin.com/in/rokbenko/" style='text-decoration: none;'>
                        <i style='color: #0072B1; margin-right: 1rem;' class="fa-xl fa-brands fa-linkedin"></i>
                    </a>
                    <a href="https://stackoverflow.com/users/10347145/" style='text-decoration: none;'>
                        <i style='color: #F48024; margin-right: 1rem;' class="fa-xl fa-brands fa-stack-overflow"></i>
                    </a>
                    <a href="https://github.com/rokbenko" style='text-decoration: none;'>
                        <i style='color: #FFFFFF; margin-right: 1rem;' class="fa-xl fa-brands fa-github"></i>
                    </a>
                    <a href="https://www.youtube.com/@rokbenko?sub_confirmation=1" style='text-decoration: none;'>
                        <i style='color: #FF0000; margin-right: 1rem;' class="fa-xl fa-brands fa-youtube"></i>
                    </a>
                    <a href="https://www.patreon.com/rokbenko" style='text-decoration: none;'>
                        <i style='color: #F96854;' class="fa-xl fa-brands fa-patreon"></i>
                    </a>
                </div>
            """,
            unsafe_allow_html=True,
        )

# Sidebar content
with st.sidebar:
    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

    with col2:
        # Display OpenAI badge
        st.image(
            "assets/images/powered-by-openai-badge-outlined-on-dark.svg", width=150
        )

    # Disclaimer about potential assistant errors
    st.markdown(
        "<div style='text-align: center; margin-bottom: 0.5rem; font-size: 0.75rem; line-height: 1rem;'>The assistant can make mistakes. Check important info.</div>",
        unsafe_allow_html=True,
    )

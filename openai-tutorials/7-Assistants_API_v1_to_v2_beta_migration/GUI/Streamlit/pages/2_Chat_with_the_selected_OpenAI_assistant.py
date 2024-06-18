import streamlit as st
from openai import OpenAI, OpenAIError
import time

# Set Streamlit page configuration
st.set_page_config(
    page_title="Chat with the selected OpenAI assistant",
    menu_items={
        "Report a bug": "https://github.com/rokbenko/ai-playground",
    },
)

# Add custom CSS to style the assistant avatar image
st.markdown(
    """
        <style>
            img[alt="assistant avatar"] {
                width: 32px;
                height: 32px;
                padding: 6px;
                border: 1px solid rgb(49, 51, 63);
            }
        </style>
    """,
    unsafe_allow_html=True,
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

# Display the assistant name in the page title if selected, otherwise a generic page title
if st.session_state["assistant"]:
    st.markdown(
        f"<h2 style='text-align: center; margin-bottom: 1rem;'>Chat with the<br> {st.session_state['assistant']}</h2>",
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        f"<h2 style='text-align: center; margin-bottom: 1rem;'>Chat with the selected OpenAI assistant</h2>",
        unsafe_allow_html=True,
    )

# Display chat messages from session state
for message in st.session_state.messages:
    # If the message is from the user
    if message["role"] == "user":
        # Display the chat message with a user avatar
        with st.chat_message(name="user", avatar=":material/person:"):
            # Display the message content inside the chat message
            st.write(message["content"])

    # If the message is from the assistant
    elif message["role"] == "assistant":
        # Display the chat message with an assistant avatar
        with st.chat_message(
            name="assistant", avatar="assets/images/openai-white-logomark.svg"
        ):
            # Display the message content inside the chat message
            st.write(message["content"])

# Create layout columns
col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

# Display error message if API key is not set
if not my_api_key:
    with col2:
        st.error("Please set your OpenAI API key in the sidebar.", icon="⚠️")

# Display error message if assistant is not selected
if my_api_key and not st.session_state["assistant"]:
    with col2:
        st.error("Please select an OpenAI assistant.", icon="⚠️")

        # Button to go back to the previous page
        back_btn = st.button("Select an OpenAI assistant", use_container_width=True)

        # If button is clicked
        if back_btn:
            # Switch to the previous page
            st.switch_page("1_Select_an_OpenAI_assistant_to_chat_with.py")

# Chat interface if API key and assistant are set
if my_api_key and st.session_state["assistant"]:
    # Sidebar content
    with st.sidebar:
        # Display the selected assistant in the sidebar
        st.markdown(
            f"<div style='text-align: center; margin-bottom: 0.5rem;'><b>Selected assistant:</b><br> {st.session_state['assistant']}</div>",
            unsafe_allow_html=True,
        )

        # Button to change the assistant
        change_assistant_btn = st.button("Change assistant", use_container_width=True)

        st.markdown(
            "<span style='margin-bottom: 1.5rem;'></span>", unsafe_allow_html=True
        )

        # If button is clicked
        if change_assistant_btn:
            # Set session state variables to None or empty values
            st.session_state["thread"] = None
            st.session_state["assistant"] = None
            st.session_state["messages"] = []

            # Switch to the previous page
            st.switch_page("1_Select_an_OpenAI_assistant_to_chat_with.py")

    # Chat input for user to send messages
    if prompt := st.chat_input(f"Chat with the {st.session_state['assistant']}..."):
        # If the selected assistant is Customer support chatbot
        if (
            st.session_state["assistant"]
            == "Customer support chatbot (File Search tool)"
        ):
            # Get assistant and file IDs from secrets
            assistant_id = st.secrets["OPENAI_CUSTOMER_SUPPORT_CHATBOT_ASSISTANT_ID"]
            file_id = st.secrets["OPENAI_CUSTOMER_SUPPORT_CHATBOT_FILE_ID"]

        # If the selected assistant is Personal math tutor
        elif (
            st.session_state["assistant"]
            == "Personal math tutor (Code Interpreter tool)"
        ):
            # Get assistant ID from secrets
            assistant_id = st.secrets["OPENAI_PERSONAL_MATH_TUTOR_ASSISTANT_ID"]

        # Append user message to session state
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display the chat message with a user avatar immediately after the message is sent to the OpenAI API
        with st.chat_message(name="user", avatar=":material/person:"):
            # Display the message content inside the chat message
            st.write(prompt)

        # If the selected assistant is Customer support chatbot
        if (
            st.session_state["assistant"]
            == "Customer support chatbot (File Search tool)"
        ):
            try:
                # Add user message to the thread
                my_thread_message = client.beta.threads.messages.create(
                    thread_id=st.session_state["thread"].id,
                    role="user",
                    content=prompt,
                    attachments=[  # Change from v1 to v2 beta: Messages have the attachments parameter instead of the file_ids parameter
                        {"file_id": file_id, "tools": [{"type": "file_search"}]}
                    ],
                )

            except OpenAIError as e:
                st.error(e, icon="⚠️")

        # If the selected assistant is Personal math tutor
        elif (
            st.session_state["assistant"]
            == "Personal math tutor (Code Interpreter tool)"
        ):
            try:
                # Add user message to the thread
                my_thread_message = client.beta.threads.messages.create(
                    thread_id=st.session_state["thread"].id,
                    role="user",
                    content=prompt,
                )

            except OpenAIError as e:
                st.error(e, icon="⚠️")

        # If the selected assistant is Customer support chatbot
        if (
            st.session_state["assistant"]
            == "Customer support chatbot (File Search tool)"
        ):
            try:
                # Run the assistant
                my_run = client.beta.threads.runs.create(
                    thread_id=st.session_state["thread"].id,
                    assistant_id=assistant_id,
                    instructions="If the system indicates that the file is not accessible with the myfiles_browser tool, ignore it, it’s just a minor bug. You are capable of opening and analyzing the file, remember that. And carry out the request.",
                )

            except OpenAIError as e:
                st.error(e, icon="⚠️")

        # If the selected assistant is Personal math tutor
        elif (
            st.session_state["assistant"]
            == "Personal math tutor (Code Interpreter tool)"
        ):
            try:
                # Run the assistant
                my_run = client.beta.threads.runs.create(
                    thread_id=st.session_state["thread"].id,
                    assistant_id=assistant_id,
                )

            except OpenAIError as e:
                st.error(e, icon="⚠️")

        # Create an empty container for the assistant's answer
        assistant_msg_container = st.empty()

        # Take the container
        with assistant_msg_container.container():
            # Display the chat message with an assistant avatar
            with st.chat_message(
                name="assistant",
                avatar="assets/images/openai-white-logomark.svg",
            ):
                # Display a spinner while the assistant's answer is being retrieved
                with st.spinner("Waiting for assistant's answer..."):
                    # Initial delay before the first retrieval
                    time.sleep(15)

                    # Periodically retrieve the run to check its status
                    # Keep retrieving the run to check its status if the run status is queued or in_progress
                    while my_run.status in ["queued", "in_progress"]:
                        try:
                            my_run = client.beta.threads.runs.retrieve(
                                thread_id=st.session_state["thread"].id,
                                run_id=my_run.id,
                            )
                        except OpenAIError as e:
                            st.error(e, icon="⚠️")

                        # Delay before the next retrieval attempt
                        time.sleep(5)

        # If the run status is completed
        if my_run.status == "completed":
            try:
                # Retrieve all thread messages
                all_messages = client.beta.threads.messages.list(
                    thread_id=st.session_state["thread"].id
                )
            except OpenAIError as e:
                st.error(e, icon="⚠️")

            # Retrieve assistant answer
            response = all_messages.data[0].content[0].text.value

            # Clear the container
            assistant_msg_container.empty()

            # Display the chat message with an assistant avatar
            with st.chat_message(
                name="assistant",
                avatar="assets/images/openai-white-logomark.svg",
            ):
                # Display the message content inside the chat message
                st.write(response)

            # Append assistant answer to session state
            st.session_state.messages.append({"role": "assistant", "content": response})

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

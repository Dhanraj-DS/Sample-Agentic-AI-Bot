import streamlit as st

st.set_page_config(page_title="Gemini Voice Assistant", page_icon="🤖", layout="centered")

st.markdown(
    """
    <h1 style='text-align:center; color:#4A90E2;'>🤖 Gemini Voice Assistant</h1>
    <p style='text-align:center; font-size:18px; color:#777;'>
        Speak your message, get intelligent replies with voice output.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

with st.expander("🎤 How to Use", expanded=True):
    st.markdown(
        """
        1. Click **Start Recording** and speak your query clearly into the microphone.<br>
        2. Click **Process Voice Input** to transcribe, send to Gemini, and get the reply.<br>
        3. Listen to the AI response played back automatically.<br>
        4. Repeat as needed for a conversation.<br>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# Display microphone widget placeholder (replace with streamlit-webrtc or custom integration)
mic_container = st.empty()
with mic_container.container():
    st.markdown("**🎙️ Voice Input:**")
    mic_button = st.button("Start Recording")

st.markdown("---")

process_button_container = st.container()
with process_button_container:
    st.markdown("**🔄 Process Interaction:**")
    process_button = st.button("Process Voice Input")

st.markdown("---")

conversation_container = st.container()
with conversation_container:
    st.markdown("**💬 Conversation:**")
    # Placeholder for displaying conversation, e.g. loops through st.session_state.messages

    if "messages" in st.session_state and st.session_state.messages:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f"<div style='background-color:#E1F5FE; padding:10px; border-radius:8px;'>**You:** {msg['content']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='background-color:#FFE0B2; padding:10px; border-radius:8px;'>**Assistant:** {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.info("No conversation yet. Start by recording your voice!")

st.markdown("---")

st.markdown("<footer style='text-align:center; color:#AAA; font-size:12px;'>Powered by Google Gemini and Streamlit</footer>", unsafe_allow_html=True)

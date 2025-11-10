import os
import streamlit as st
from dotenv import load_dotenv

# Import the official Google Gemini AI SDK client
from google import genai
from google.genai import types

# Load environment variables from .env.local
load_dotenv(".env.local")

# Get Gemini API key from environment
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("Google API key is missing. Please set it in .env.local")
    st.stop()

# Initialize Gemini client
client = genai.Client()

st.set_page_config(page_title="Gemini AI Assistant", page_icon="🤖", layout="centered")
st.title("Gemini AI Assistant")

# Initialize message history if not present
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input text box
user_input = st.text_input("You:", key="input")

if st.button("Send"):
    if not user_input.strip():
        st.warning("Please enter a message.")
    else:
        # Append user message to conversation
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Prepare messages for Gemini API in expected format, commonly strings or list of contents
        conversation_prompt = "\n".join(
            f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state.messages
        )

        try:
            # Call Gemini model with the prompt
            response = client.models.generate_content(
                model="gemini-2.5-flash",  # Use a valid Gemini model ID
                contents=[conversation_prompt],
                config=types.GenerateContentConfig(
                    temperature=0.7,
                    max_output_tokens=512,
                ),
            )
            assistant_reply = response.text

            # Append assistant's reply to conversation
            st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

        except Exception as e:
            st.error(f"Error calling Gemini API: {e}")

# Display chat messages with basic styling
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div style='background-color:#26c7dc; padding:9px; border-radius:6px; margin-bottom:5px;'><b>You:</b> {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='background-color:#26c7dc; padding:8px; border-radius:6px; margin-bottom:5px;'><b>Assistant:</b> {msg['content']}</div>", unsafe_allow_html=True)

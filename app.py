import streamlit as st
from dotenv import load_dotenv
from core.openai_client import ask_gpt
from core.azure_speech import speech_to_text, text_to_speech, stop_speaking

load_dotenv()

st.set_page_config(page_title="Voice Chatbot", layout="centered")
st.title(" Azure OpenAI Chatbot with Voice")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Text input (typed by user) ---
if prompt := st.chat_input("Type your message or click '🎤 Speak'"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking…"):
        answer = ask_gpt(prompt)

    # Always show the answer
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)

    # Optionally speak (you can remove this if you prefer manual trigger)
    text_to_speech(answer)

# --- Voice input (spoken by user) ---
if st.button(" Speak"):
    spoken = speech_to_text()
    if spoken:
        st.write(f"**You said:** {spoken}")

        with st.spinner("Thinking…"):
            answer = ask_gpt(spoken)

        # Always show the answer
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.markdown(answer)

        # Speak it
        text_to_speech(answer)

# --- Skip Talking button ---
if st.button(" Skip Talking"):
    stop_speaking()
    st.info("Stopped speaking (message still shown above).")

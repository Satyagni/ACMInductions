import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("🧠 Groq-Powered Chatbot")

model = st.selectbox(
    "Choose a model:",
    ["mistral-saba-24b", "llama-3.1-8b-instant", "gemma2-9b-it"],
    index=0
)

if st.button("🔄 Clear Chat"):
    st.session_state.history = []

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Say something...")

if user_input:
    with st.spinner("Bot is thinking..."):
        response = get_response(user_input, model)
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Bot", response))

for speaker, message in st.session_state.history:
    with st.chat_message(speaker):
        st.markdown(message)

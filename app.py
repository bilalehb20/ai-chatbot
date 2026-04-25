"""
Streamlit web app for the Mini AI Chatbot.
This makes it easy for teachers to test the chatbot in a browser.
"""

import streamlit as st

from main import classify_intent, generate_response


st.set_page_config(page_title="Mini AI Chatbot", page_icon="🤖")
st.title("🤖 Mini AI Chatbot")
st.caption("Rule-based chatbot - school portfolio demo")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hoi! Ik ben je mini AI-chatbot. Stel een vraag of typ 'help'.",
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_prompt = st.chat_input("Typ je vraag hier...")

if user_prompt:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    intent = classify_intent(user_prompt)
    bot_reply = generate_response(intent)

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

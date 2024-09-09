import streamlit as st
from langchain.schema import ChatMessage

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        ChatMessage(role="assistant", content="Привет!✌️ Я X6, ваш личный ассистент, который знает (почти) все о внутрикорпоративных тонкостях. Подскажите, чем я могу быть полезен?")
    ]

for message in st.session_state.messages:
    with st.chat_message(message.role):
        st.markdown(message.content)

if prompt := st.chat_input("Напишите ваш вопрос"):
    message = ChatMessage(role="user", content=prompt)
    st.session_state["messages"].append(message)

    with st.chat_message("user"):
        st.markdown(message.content)

    message = ChatMessage(role="assistant", content="")
    st.session_state["messages"].append(message)

    with st.chat_message("assistant"):
        with st.spinner("Обрабатываю ваш запрос..."):
            message_placeholder = st.empty()
            message_placeholder.markdown("Вот что я нашел по вашему запросу:")

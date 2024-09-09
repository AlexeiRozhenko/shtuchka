import streamlit as st
from langchain.schema import ChatMessage

to_server = {
        "server_query": "zatychka",
    }
# Получение ответа от сервера
def send_request(url, payload):
    """Send request to FastAPI server"""
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            st.write(f"{response.json()}")
        else:
            st.write(
                f"Нет ответа от FastAPI сервера ({url}). Код статуса: {response.status_code}"
            )
    except Exception as e:
        st.write(f"Произошла ошибка: {e}")

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

    message = ChatMessage(role="assistant", content="zatychka")
    st.session_state["messages"].append(message)

    with st.chat_message("assistant"):
        with st.spinner("Обрабатываю ваш запрос..."):
            message_placeholder = st.empty()
            message_placeholder.markdown("Вот что я нашел по вашему запросу:")

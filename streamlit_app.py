import streamlit as st
import requests
from langchain.schema import ChatMessage

address = "http://95.182.121.46:8080/query?query=%D0%9A%D0%B0%D0%BA%20%D1%82%D0%B2%D0%BE%D0%B8%20%D0%B4%D0%B5%D0%BB%D0%B0"

# Отправление запроса на FastAPI сервер
def send_request(url, to_server):
  try:
    response = requests.get(url, json=to_server)
    if response.status_code == 200:
      st.write(f"{response.json()}")
    else:
      st.write(
      f"Нет ответа от FastAPI сервера ({url}). Код статуса: {response.status_code}"
              )
  except Exception as e:
    st.write(f"Произошла ошибка: {e}")

st.subheader("Техническая поддержка X5", divider="green")

# Вводное сообщение от чатбота
if "messages" not in st.session_state:
  st.session_state["messages"] = [ChatMessage(role="assistant", content="Привет!✌️ Я X6, ваш личный ассистент, который знает (почти) все о внутрикорпоративных тонкостях. Подскажите, чем я могу быть полезен?")]

# Выведение истории чата 
for message in st.session_state.messages:
  if message.role == "assistant":
    with st.chat_message(message.role, avatar="🖥️"):
      st.text(message.content)

# Инициализация окна ввода информации для пользователя
if prompt := st.chat_input("Напишите ваш вопрос"):
  message = ChatMessage(role="user", content=prompt)
  st.session_state["messages"].append(message)

  with st.chat_message("user", avatar="🦖"):
    st.text(message.content)

  message = ChatMessage(role="assistant", content="pass")
  st.session_state["messages"].append(message)

# Генерация ответа ассистента и получение ответа с FastAPI сервера
  with st.chat_message("assistant", avatar="🖥️"):
    with st.spinner("Обрабатываю ваш запрос..."):
      data = message.content
      server_answer = send_request(address, data)
      # server_answer = "pass"
      message_placeholder = st.empty()
      message_placeholder.text(f"Вот что я нашел по вашему запросу:\n{prompt}")

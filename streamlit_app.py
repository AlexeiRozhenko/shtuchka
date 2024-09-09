import streamlit as st
from langchain.schema import ChatMessage

address = "pass"

# Отправление запроса на FastAPI сервер
def send_request(url, to_server):
  try:
    response = requests.post(url, json=to_server)
    if response.status_code == 200:
      st.write(f"{response.json()}")
    else:
      st.write(
      f"Нет ответа от FastAPI сервера ({url}). Код статуса: {response.status_code}"
              )
  except Exception as e:
    st.write(f"Произошла ошибка: {e}")

# Вводное сообщение от чатбота
if "messages" not in st.session_state:
  st.session_state["messages"] = [
  ChatMessage(role="assistant", content="Привет!✌️ Я X6, ваш личный ассистент, который знает (почти) все о внутрикорпоративных тонкостях. Подскажите, чем я могу быть полезен?")
  ]

# Выведение истории чата 
for message in st.session_state.messages:
  with st.chat_message(message.role):
    st.markdown(message.content)

# Инициализация окна ввода информации для пользователя
if prompt := st.chat_input("Напишите ваш вопрос"):
  message = ChatMessage(role="user", content=prompt)
  st.session_state["messages"].append(message)

  with st.chat_message("user"):
    st.markdown(message.content)

  message = ChatMessage(role="assistant", content="pass")
  st.session_state["messages"].append(message)

# Генерация ответа ассистента и получение ответа с FastAPI сервера
with st.chat_message("assistant"):
  with st.spinner("Обрабатываю ваш запрос..."):
    data = {"server_query": message.content}
    server_answer = send_request(address, data)
    message_placeholder = st.empty()
    message_placeholder.markdown(f"Вот что я нашел по вашему запросу:\n{server_answer}")

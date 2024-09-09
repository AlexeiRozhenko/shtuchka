import streamlit as st

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        ChatMessage(role="assistant", content="Привет! Я X6, ваш личный ассистент, который знает (почти) все-все о внутрикорпоративных тонкостях. Подскажите, чем я могу быть полезен?")
    ]

for message in st.session_state["messages"][1::1]:
    with st.chat_message(message.role):
        st.markdown(message.content)

if prompt := st.chat_input("Напишите ваш вопрос"):
    message = ChatMessage(role="user", content=prompt)
    # st.session_state["messages"].append(message)

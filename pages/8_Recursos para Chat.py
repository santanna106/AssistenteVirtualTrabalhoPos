import time
import streamlit as st

from openai import OpenAI

flai = 'recursos/logo flai com sombra.png'

st.title("🐶🐕🐩 Dog Bot")

chave = st.sidebar.text_input('Chave da API OpenAI', type = 'password')
client = OpenAI(api_key=chave)



# Iniciar Historico Chat
if "mensagens" not in st.session_state:
    st.session_state.mensagens = [{"role": 'system', "content": 'Você será um amigo cachorrinho para uma criança de 5 anos de idade. Sua função é ser um companheiro para dar conselhos sempre que a criança quiser conversar com voce. Use sempre uma linguagem positiva, alegre e abuse dos emojis!'}]


# Aparecer o Historico do Chat na tela
for mensagens in st.session_state.mensagens[1:]:
    with st.chat_message(mensagens["role"]):
        st.markdown(mensagens["content"])


# React to user input
prompt = st.chat_input("Digite alguma coisa")

if prompt:
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.mensagens.append({"role": "user", "content": prompt})

    resposta = "Sei lá"


    chamada = client.chat.completions.create(
         model = 'gpt-3.5-turbo',
         messages = st.session_state.mensagens
     )

    resposta = chamada.choices[0].message.content

    # Display assistant response in chat message container
    with st.chat_message("system"):
        st.markdown(resposta)
    # Add assistant response to chat history
    st.session_state.mensagens.append({"role": "system", "content": resposta})







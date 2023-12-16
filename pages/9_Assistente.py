from openai import OpenAI
import streamlit as st
import pandas as pd
import numpy as np

API_KEY = ''
client = OpenAI(api_key=API_KEY)
st.session_state.mensagens = []

#Cabeçalho
st.header('💜 Conteúdo da Página A')
st.title('Chat de acesso do  sistema SGS  💙')
st.header('Configuração do Chat')
st.divider()

#Formulário
st.subheader('1. Defina a criatividade da resposta')

temperature  = st.slider(label = 'Slider',
    min_value=0.,
    max_value=2.,
    value= [0.,1.], # é possivel colocar horários e datas (biblioteca datetime)
    step=0.1,
    format= '%.1f', # '%d' para inteiros, '%e' para notacao cientifica, '%f' para numeros reais
    key=None,
    help='Input numérico',
    on_change=None,
    args=None,
    kwargs=None,
    disabled=False,
    label_visibility="visible")
st.write(temperature[1] )

st.divider()
st.subheader('2. Configure o tamanho da resposta')
max_tokens_resposta = 200
genre = st.radio(
     "Tamanho da Resposta",
     ('Curta', 'Média', 'Extensa'),
     horizontal=True)

if genre == 'Curta':
     max_tokens_resposta = 100
elif genre == 'Média':
     max_tokens_resposta = 250
else:
    max_tokens_resposta = 400

st.divider()
st.subheader('3. Estilo de Escrita')

estilo_escrita = ""
estilo = st.radio(
     "Estilos",
     ('Cordial', 'Objetivo','Simples'),
     horizontal=True)


if estilo == 'Cordial':
     estilo_escrita = "cordial"
elif estilo == 'Objetivo':
     estilo_escrita = "objetivo e direto nas suas respostas"
else:
    estilo_escrita = "de linguagem simples e bem articulada"

# Fim Formulário

# Variaveis de Sessão
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "Você será um assistente" + estilo_escrita + " virtual para um usuário do sistema SGS. Sua função será tentar resolver os problemas de acesso do usuário ao SGS. Pedido para ele verificar se o usuário dele está ativo. Se ele tem permissão de acesso ao sistema e caso as verificações não sejam suficientes solicitar que o usuário entre em contato com o setor AB responsável."}
    ]

if 'model_name' not in st.session_state:
    st.session_state['model_name'] = []
if 'cost' not in st.session_state:
    st.session_state['cost'] = []
if 'total_tokens' not in st.session_state:
    st.session_state['total_tokens'] = []
if 'total_cost' not in st.session_state:
    st.session_state['total_cost'] = 0.0


# Sidebar - let user choose model, show total cost of current conversation, and let user clear the current conversation
st.sidebar.title("Sidebar")
model_name = st.sidebar.radio("Choose a model:", ("GPT-3.5", "GPT-4"))
counter_placeholder = st.sidebar.empty()
counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")
clear_button = st.sidebar.button("Clear Conversation", key="clear")

# Map model names to OpenAI model IDs
if model_name == "GPT-3.5":
    model = "gpt-3.5-turbo"
else:
    model = "gpt-4"
      
# Iniciar Historico Chat
if "mensagens" not in st.session_state:
    {"role": "system", "content": "Você será um assistente virtual para um usuário do sistema SGS. Sua função será tentar resolver os problemas de acesso do usuário ao SGS. Pedido para ele verificar se o usuário dele está ativo. Se ele tem permissão de acesso ao sistema e caso as verificações não sejam suficientes solicitar que o usuário entre em contato com o setor AB responsável."}


# Aparecer o Historico do Chat na tela
for mensagens in st.session_state.mensagens[1:]:
    with st.chat_message(mensagens["role"]):
        st.markdown(mensagens["content"])

# React to user input
prompt = st.chat_input("Está tendo algum problema com o SGS?")

if prompt:
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.mensagens.append({"role": "user", "content": prompt})

    for msg in st.session_state.mensagens:
        if msg['role'] == 'user':
        #print('Mensagem Do Menino> ',msg)
            moderation = client.moderations.create(input=msg['content'])

            output = moderation.results[0]

            df = pd.DataFrame(dict(output.category_scores).items(), columns=['Category', 'Value'])
            df.sort_values(by = 'Value', ascending = False).round(5)


            indice_max_category_value = df['Value'].idxmax()
            linha_max_category_value = df.loc[indice_max_category_value]
            category = linha_max_category_value['Category']


            lista = df[df['Value'] > 0.1]
            flag_continua_dialogo  = True
            if len(lista) > 0 :
                with st.chat_message("system"):
                    st.markdown('O diálogo desobedeceu as regras de moderação')
                flag_continua_dialogo  = False

    if flag_continua_dialogo:
        chamada = client.chat.completions.create(
            model=model,
            messages=st.session_state['messages'],
            temperature = temperature[1],
            max_tokens=max_tokens_resposta
        )
        resposta = chamada.choices[0].message.content


        # Display assistant response in chat message container
        with st.chat_message("system"):
            st.markdown(resposta)
        # Add assistant response to chat history
        st.session_state.mensagens.append({"role": "system", "content": resposta})


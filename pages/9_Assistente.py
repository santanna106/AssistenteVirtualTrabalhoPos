from openai import OpenAI
import streamlit as st
import pandas as pd
import numpy as np
import math
from time import gmtime, strftime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

API_KEY = ''
client = OpenAI(api_key=API_KEY)

def ajusta_linhas(linha:str,tam:int) -> str:
    nova_linha = linha
    tamanho = len(linha)
    num_quebras = math.ceil(tamanho / tam)
    
    num_quebras = num_quebras 
    posicao_ant = 0
    linha_tratada = ''
    for seq in range(num_quebras):
        posicao_quebra = (seq + 1)*tam
        #print(nova_linha[posicao_ant:posicao_quebra]) 
        linha_tratada = linha_tratada + nova_linha[posicao_ant:posicao_quebra] + "\n"
        posicao_ant = posicao_quebra
        
    return linha_tratada



# Função para desenhar texto com quebra de linha
def draw_text_with_line_breaks(c, x, y, text, max_width):
    text_object = c.beginText(x, y)
    text_object.setFont("Helvetica", 12)
    text_object.setTextOrigin(x, y)
    
    nova_string = ajusta_linhas(text,80)
    lines = nova_string.split("\n")  # Dividir o texto em linhas
    for line in lines:
        text_object.textLine(line)  # Adicionar cada linha ao objeto de texto

    c.drawText(text_object)
    
def converte_historico_em_string()->str:
    historico_dialogo = []
    index = 1
    for msg in st.session_state.mensagens:
        linha = f"{index}. {msg['role']}: {msg['content']}"
        historico_dialogo.append(linha)
        index = index + 1
        
    return historico_dialogo


if 'model_name' not in st.session_state:
    st.session_state['model_name'] = []
if 'cost' not in st.session_state:
    st.session_state['cost'] = []
if 'total_tokens' not in st.session_state:
    st.session_state['total_tokens'] = []
if 'total_cost' not in st.session_state:
    st.session_state['total_cost'] = 0.0
if 'data_hora_inicio_conversa' not in st.session_state:
    st.session_state['data_hora_inicio_conversa'] = ''

if 'mensagens' not in st.session_state:
    st.session_state['mensagens'] = []
    
    
    
    
# Sidebar - let user choose model, show total cost of current conversation, and let user clear the current conversation
st.sidebar.title("Sidebar")
model_name = st.sidebar.radio("Escolha o modelo:", ("GPT-3.5", "GPT-4"))
counter_placeholder = st.sidebar.empty()
counter_placeholder.write(f"Custo Total: ${st.session_state['total_cost']:.5f}")
token_placeholder = st.sidebar.empty()
token_placeholder.write(f"Total de Tokens: {sum(st.session_state['total_tokens'])}")
data_placeholder = st.sidebar.empty()
data_placeholder.write(f"Data e Hora: { st.session_state['data_hora_inicio_conversa']}")
data_frame = st.sidebar.empty()
    
    
# Map model names to OpenAI model IDs
if model_name == "GPT-3.5":
    model = "gpt-3.5-turbo"
else:
    model = "gpt-4"


if "desabilita_widget" not in st.session_state:
    st.session_state["desabilita_widget"] = False

# Adicione um botão de encerramento
if st.sidebar.button("Encerrar Conversa", key="clear", type="primary"):
    st.session_state['desabilita_widget'] = True
    counter_placeholder.write(f"Custo Total: ${st.session_state['total_cost']:.5f}")
    token_placeholder.write(f"Total de Tokens: {sum(st.session_state['total_tokens'])}")
    data_placeholder.write(f"Data e Hora: { st.session_state['data_hora_inicio_conversa']}")
    historico_da_conversa = '\n'.join(converte_historico_em_string())
    data_info_chat = {'TotalCusto': [f"${st.session_state['total_cost']:.5f}"],
                      'TotalTokens': [sum(st.session_state['total_tokens'])],
                      'DataHora':[st.session_state['data_hora_inicio_conversa']],
                      'Historico':historico_da_conversa
                      }  
    
    df = pd.DataFrame(data_info_chat) 
    data_frame.write(df)
    st.divider()
    
   

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
            label_visibility="visible",
            disabled=st.session_state['desabilita_widget']
)
          
st.subheader('2. Configure o tamanho da resposta')
max_tokens_resposta = 200
genre = st.radio(
     "Tamanho da Resposta",
     ('Curta', 'Média', 'Extensa'),
     horizontal=True,
     disabled=st.session_state['desabilita_widget']
     )

if genre == 'Curta':
     max_tokens_resposta = 100
elif genre == 'Média':
     max_tokens_resposta = 250
else:
    max_tokens_resposta = 400
    
st.subheader('3. Estilo de Escrita')

estilo_escrita = ""
estilo = st.radio(
     "Estilos",
     ('Cordial', 'Objetivo','Simples'),
     horizontal=True,
     disabled=st.session_state['desabilita_widget']
     )


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



# Aparecer o Historico do Chat na tela
for mensagens in st.session_state.mensagens[1:]:
    with st.chat_message(mensagens["role"]):
        st.markdown(mensagens["content"])


# React to user input
prompt = st.chat_input("Está tendo algum problema com o SGS?", disabled=st.session_state['desabilita_widget'])



if prompt:

    if len(st.session_state.mensagens) == 0:
        data_hora_inicio_conversa = strftime("%a, %d/%m/%Y %H:%M ", gmtime())
        st.session_state['data_hora_inicio_conversa'] = strftime("%a, %d/%m/%Y %H:%M ", gmtime())

        st.write("Conversa Iniciada em: " + st.session_state['data_hora_inicio_conversa'])
    
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

        total_tokens = chamada.usage.total_tokens
        prompt_tokens = chamada.usage.prompt_tokens
        completion_tokens = chamada.usage.completion_tokens

        st.session_state['total_tokens'].append(total_tokens)
        if model_name == "GPT-3.5":
            cost = total_tokens * 0.002 / 1000
        else:
            cost = (prompt_tokens * 0.03 + completion_tokens * 0.06) / 1000

        st.session_state['cost'].append(cost)
        st.session_state['total_cost'] += cost

        st.write(st.session_state['total_cost'])


        # Display assistant response in chat message container
        with st.chat_message("system"):
            st.markdown(resposta)
        # Add assistant response to chat history
        st.session_state.mensagens.append({"role": "system", "content": resposta})
        
        

    
    
    #st.stop()
    

if st.session_state["desabilita_widget"]:
    if st.sidebar.button("Exportar Diálogo"):
        pdf_filename = "historico/historico_conversa.pdf"
        c = canvas.Canvas(pdf_filename, pagesize=A4)
        c.setFont("Helvetica", 12)
       
        
        if len(st.session_state.mensagens) == 0:
            c.drawString(50, 700, f"1: Não existiu diálogo neste chat")
            c.showPage()
         
            

        # Write chat messages to the PDF
        index = 1
        x = 50
        y = A4[1] - 50  # Margem superior
        # Largura máxima para o texto (ajuste conforme necessário)
        largura_maxima = A4[0] - 2 * x  # Use a largura da página com margens

        for msg in st.session_state.mensagens:
            linha = f"{index}. {msg['role']}: {msg['content']}"
            draw_text_with_line_breaks(c, x, y, linha, largura_maxima)

            #c.drawString(x, y, linha)
            y -= 20  # Mude a posição y para a próxima linha
            index=index+1
            
        c.save()

        st.success(f"PDF generated successfully: [Download PDF]({pdf_filename})")
        



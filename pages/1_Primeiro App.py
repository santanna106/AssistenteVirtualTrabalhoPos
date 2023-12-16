import streamlit as st 

st.header('💜 Conteúdo da Página A')
st.title('Meu Primeiro Aplicativo Streamlit 💙')
st.header('Meu Primeiro Aplicativo Streamlit')
st.write('Meu Primeiro Aplicativo Streamlit')


botao = st.button('Clica em mim')

#input do front-end
numero = st.slider('Escolha um número')

#back-end
frase = f'O número selecionado é {numero} e seu quadrado é {numero**2}'

#resposta de volta ao front-end
st.write(frase)


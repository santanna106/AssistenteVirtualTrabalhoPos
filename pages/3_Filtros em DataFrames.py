import streamlit as st 

st.header('💙 Conteúdo da Página C')

import pandas as pd
link = 'https://raw.githubusercontent.com/ricardorocha86/Datasets/master/Titanic/train.csv'
dados = pd.read_csv(link)

#st.write(dados)

s = st.checkbox('Assinale se quiser apenas sobreviventes')

n1, n2 = st.slider('Idades para filtrar', 
	min_value = 20, 
	max_value = 80,
	value = [40, 60])

filtro1 = dados['Age'] >= n1
filtro2 = dados['Age'] <= n2
filtro3 = dados['Survived'] == 1

if s:
	st.write(dados.loc[filtro1 & filtro2 & filtro3, :])
else:
	st.write(dados.loc[filtro1 & filtro2, :])


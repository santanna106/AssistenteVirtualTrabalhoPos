import streamlit as st 

st.header('💫 A mágica do Streamlit')

n = st.number_input(
	label = 'Entre com um número',
	min_value = 100,
	max_value = 2000,
	step = 100,
	value = 100,
	help = 'Instrução para o widget')

titulo = st.text_input(
	label = 'Entre com o título',
	max_chars = 100,
	placeholder = 'Texto cinzinha')


cor = st.color_picker('Escolha a cor do gráfico')

import numpy as np 
import matplotlib.pyplot as plt

seq = np.random.normal(size = n)

plt.hist(seq, color = cor, edgecolor = 'white')
plt.title(titulo)

st.write(cor)
st.pyplot(plt)
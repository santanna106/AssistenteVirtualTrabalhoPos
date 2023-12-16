import streamlit as st 
import pandas as pd
import numpy as np
from pycaret.regression import load_model, predict_model
from pycaret.datasets import get_data

dados = get_data('insurance')
modelo = load_model('recursos/modelo-previsao-custos-seguro')

def trad(x):
	return 'Masculino' if x == 'male' else 'Feminino'

def trad2(x):
	return 'Sim' if x == 'yes' else 'Não'



st.header('Deploy do Modelo de Previsão de Custos de Seguro')
st.write('Entre com as caracteristicas da pessoa para fazer uma previsão de custos de seguro para ela.')



#Widgets para fazer os inputs do modelo

col0, col1, col2, col3 = st.columns([0.5,3,3,3])

with col0:
	c = st.checkbox(label = 'Assinale a caixa ao lado', 
	 	help='Caixa de assinalar', 
		args=['Você clicouuuuu'], 
		value = True,
		kwargs=None,
	 	disabled=False, 
	 	label_visibility="collapsed") #hidden #collapsed

with col1:
	age = st.slider(label = 'Idade', 
		min_value=18, 
		max_value=64, 
		value= 40, 
		step=1, 
		help='Entre com a idade do indivíduo',
		disabled = not c)

	bmi	= st.number_input(label = 'IMC', 
		min_value = 16., 
		max_value = 53., 
		value = 30., 
		step = 0.1)


with col2: 
	children = st.select_slider(label = 'Dependentes', 
		options = [0,1,2,3,4,5])	
	region = st.selectbox(label = 'Região', 
		options = dados['region'].unique())

with col3:
	sex	= st.radio('Sexo', ['male', 'female'], format_func = trad)
	smoker = st.radio('Fumante', ['yes', 'no'], format_func = trad2)





#Criar um DataFrame com os inputs exatamente igual ao dataframe em que foi treinado o modelo
aux = {'age': [age if c else np.NaN],
		'sex': [sex],
		'bmi': [bmi],
		'children': [children],
		'smoker': [smoker],
		'region': [region]}

prever = pd.DataFrame(aux)

st.write(prever)

#Usar o modelo salvo para fazer previsao nesse Dataframe

_, c1, _ = st.columns([2,3,1])

with c1:
	botao = st.button('Calcular custos de seguro',
		type = 'primary',
		use_container_width = True)

if botao:
	previsao = predict_model(modelo, data = prever)
	valor = round(previsao.loc[0,'prediction_label'], 2)
	st.write(f'### O custo previsto pelo modelo é de ${valor}')


inputs = []

for i in range(5):
	inputs.append(st.selectbox(f'Variavel {i}', [f'A{i}', f'B{i}', f'C{i}']))

st.write(inputs)
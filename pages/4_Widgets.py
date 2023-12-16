import streamlit as st 

st.header('💙 Widgets')

def acao(texto):
	st.write(f'{texto}')

botao = st.button(label = 'Clique em mim!',
	key = None, 
	help = 'Instruções para quando o usuário repousa o mouse em cima do botão',
	type = 'primary', # 'primary' ou 'secondary'
	disabled = False,
	use_container_width = True,
	on_click = acao,
	args = None,
	kwargs = {'texto': 'Você clicou!'}
) 

st.subheader('2. Checkbox')

checkbox = st.checkbox(label = 'Assinale a caixa ao lado', 
 	value=True, 
 	key=None, 
 	help='Caixa de assinalar', 
 	on_change = acao, 
	args=['Você clicouuuuu'], 
	kwargs=None,
 	disabled=False, 
 	label_visibility="visible") #hidden #collapsed

st.write(checkbox) 



st.subheader('1. Radio')
def traducao(x):
	dicionario = {
		'male': 'Masculino',
		'female': 'Feminino',
		'other': 'Outro'
	}
	return dicionario.get(x)

radio = st.radio(label = 'Botões de radio', 
	options = ['male', 'female', 'other'] , 
	index = 2, 
	format_func = traducao, 
	key = None, 
	help = 'Escolha um botão', 
	on_change = None,  
	args=None, 
	kwargs=None,
	disabled = False, 
	horizontal = False, 
	label_visibility = "collapsed") #hidden #collapsed

st.write(radio)



st.divider()
st.subheader('2. Selection Slider')

s = st.select_slider(label = 'Slider de Seleção', 
	options = ['male', 'female', 'other'], 
	value = 'female', 
	format_func = traducao, 
	key=None, 
	help='Slider de Seleção', 
	on_change=None, 
	args=None, 
	kwargs=None,
	disabled=False, 
	label_visibility="visible")

st.write(s) 


st.divider()
st.subheader('3. Selectbox')

selecao = st.selectbox(label = 'Caixa de Seleção', 
	options = ['male', 'female', 'other'] ,
	index = 1, 
	format_func = traducao, 
	key = None, 
	help = 'Caixa de Seleção', 
	on_change = None, 
	args=None, 
	kwargs=None,
	disabled = False, 
	label_visibility = "visible")

st.write(selecao) 


st.divider()
st.subheader('4. Multiselect')

multipla = st.multiselect(label = 'Caixa de Seleção Multipla', 
	options = ['male', 'female', 'other'], 
	default = ['male', 'female'], 
	format_func = traducao, 
	key=None, 
	help = 'Caixa de Seleção Múltipla', 
	on_change=None, 
	args=None, 
	kwargs=None,
	disabled=False, 
	label_visibility="visible", 
	max_selections = 3)

st.write(multipla) 



st.subheader('1. Slider')

n = st.slider(label = 'Slider', 
	min_value=10., 
	max_value=50., 
	value= [20.,30.], # é possivel colocar horários e datas (biblioteca datetime)
	step=1.61803, 
	format= '%.1f', # '%d' para inteiros, '%e' para notacao cientifica, '%f' para numeros reais
	key=None, 
	help='Input numérico', 
	on_change=None, 
	args=None, 
	kwargs=None,
	disabled=False, 
	label_visibility="visible")

st.write(n) 

st.divider()
st.subheader('2. Number Input')

numero = st.number_input(label = 'Entre com um número', 
	min_value = 2., 
	max_value = 75., 
	value = 10., 
	step = 3.5, 
	format = "%.1f", # '%d' para inteiros, '%e' para notacao cientifica, '%f' para numeros reais
	key = None, 
	help = 'Input Numérico', 
	on_change = None, 
	args = None, 
	kwargs = None, 
	disabled = False, 
	label_visibility = "visible")

st.write(numero) 



st.subheader('1. Text Input')

texto = st.text_input(label = 'Input de Texto', 
	value="", 
	max_chars=30, 
	key=None, 
	type="password", #"default" ou "password"
	help='Texto de ajuda', 
	autocomplete=None, 
	on_change=None, 
	args=None, 
	kwargs=None,
	placeholder='Digite a sua senha', 
	disabled=False, 
	label_visibility="visible")
 
st.write(texto) 

st.divider()

st.subheader('2. Text Area')

texto = st.text_area(label = 'Texto grande', 
	value="", 
	height=10, 
	max_chars=1000, 
	key=None, 
	help='Texto', 
	on_change=None, 
	args=None, 
	kwargs=None, 
	placeholder='Digite a sua história', 
	disabled=False, 
	label_visibility="visible") # "visible" ou "hidden" ou "collapsed"

st.write(texto) 



st.subheader('1. Date Input')

import datetime 

data = st.date_input(label = 'Escolha uma data', 
	value = [datetime.date(2025, 10, 10), datetime.date(2025, 10, 20)], 
	min_value = datetime.date(2025, 9, 29), 
	max_value = datetime.date(2025, 11, 29), 
	key=None, 
	help='Ajuda', 
	on_change=None, 
	args=None, 
	kwargs=None,
	disabled=False, 
	label_visibility="visible")

st.write(data[0].strftime('%d/%m/%Y')) 
st.write(data[1].strftime('%d/%m/%Y')) 

st.divider()

st.subheader('2. Time Input')

hora = st.time_input(label = 'Escolha uma hora', 
	value = datetime.time(10,10), 
	key=None, 
	help='Ajuda', 
	on_change=None, 
	args=None, 
	kwargs=None, 
	disabled=False, 
	label_visibility="visible", 
	step=300)

st.write(hora) 


st.subheader('1. File Uploader')

arquivo = st.file_uploader(label = 'Carregue seu arquivo', 
	type='csv', 
	accept_multiple_files=False, 
	key=None, 
	help='Ajuda', 
	on_change=None, 
	args=None, 
	kwargs=None, 
	disabled=False, 
	label_visibility="visible")

st.write(arquivo)

if arquivo is not None:
	import pandas as pd 

	dados = pd.read_csv(arquivo)
	st.write(dados.head(5))

	sal = dados["salario"].value_counts()	
	st.write(sal)

	fig = dados["idade"].plot(kind = 'hist', edgecolor = 'black')
	fig.get_figure().savefig('gráfico.png')

	st.image('gráfico.png')



st.divider()

st.subheader('2. Download Button')

st.download_button(label = 'Clique para baixar', 
	data = 'sds', 
	file_name='salarios.csv', 
	mime='text/csv', 
	key=None, 
	help='Ajuda', 
	on_click=None, 
	args=None, 
	kwargs=None,
	disabled=False, 
	use_container_width=False)

st.subheader('1. Color Picker')

cor = st.color_picker(label = 'Escolha uma cor', 
	value='#0f54c9', 
	key=None, 
	help='Ajuda', 
	on_change=None, 
	args=None, 
	kwargs=None, 
	disabled=False, 
	label_visibility="visible")

st.write(cor) 


st.divider()

st.subheader('2. Camera Input')

cam = st.camera_input(label = 'Tire uma foto', 
	key=None, 
	help=None, 
	on_change=None, 
	args=None, 
	kwargs=None, 
	disabled=False, 
	label_visibility="visible") 

st.write(cam) 


st.divider()

st.subheader('3. Data Editor')

import pandas as pd 

dic = {'Nomes': ['João', 'Maria'],
	   'Idades': [25, 35]}

dados = pd.DataFrame(dic)

#st.write(dados)

novo = st.data_editor(data = dados, 
	width=400, 
	height=200, 
	use_container_width=True, 
	hide_index=False,     
	column_order=['Idades', 'Nomes'], 
	column_config=None, 
	num_rows="dynamic", 
	disabled=False, 
	key=None, 
	on_change=None, 
	args=None, 
	kwargs=None)
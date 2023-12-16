import streamlit as st 

st.header('💙 Abas e Colunas')

col1, col2 = st.columns(2)

with col1:
	st.header('Coluna 1')
	st.write('Coluna da esquerda udhauef ufhda uhfeau uhfeau hfua hfuahfeahfeuahfua hu hfau hfuea hau hfeau ')

with col2:
	st.header('Coluna 2')
	st.write('Coluna da direita udhauef ufhda uhfeau uhfeau hfua hfuahfeahfeuahfua hu hfau hfuea hau hfeau ')


st.markdown('---')


col1, col2 = st.columns([1,2])

with col1:
	st.header('Coluna 1')
	st.write('Coluna da esquerda udhauef ufhda uhfeau uhfeau hfua hf uahfea hfeua hfua hu hfau hfuea hau hfeau ')

with col2:
	st.header('Coluna 2')
	st.write('Coluna da direita udhauef ufhda uhfeau uhfeau hfua hfuahf eahf euah fua hu hfau hfuea hau hfeau ')


	c1, c2 = st.columns([2,1])

	with c1:
		st.subheader('SubColuna 1')
		st.write('Coluna da esquerda udhauef ufhda uhfeau uhfeau hfua hfuahfeahfeuahfua hu hfau hfuea hau hfeau ')

	with c2:
		st.subheader('SubColuna 2')
		st.write('Coluna da direita udhauef ufhda uhfeau uhfeau hfua hfuahfeahfeuahfua hu hfau hfuea hau hfeau ')







st.markdown('---')

st.title('Abas')

abas = ['💙 Aba A', '🧡 Aba B', '❤ Aba C']

aba1, aba2, aba3 = st.tabs(abas)


with aba1:
	st.header('Aba 1')
	st.write('Coluna da aba 1 udhauef ufhda uhfeau uhfeau hfua hfuahfeahfeuahfua hu hfau hfuea hau hfeau ')


with aba2:
	st.header('Aba 2')
	st.write('Coluna da aba 2 udhauef ufhda uhfeau uhfeau hfua hfuahfeahfeuahfua hu hfau hfuea hau hfeau ')


with aba3:
	st.header('Aba 3')
	st.write('Coluna da aba 3 udhauef ufhda uhfeau uhfeau hfua hfuahfeahfeuahfua hu hfau hfuea hau hfeau ')




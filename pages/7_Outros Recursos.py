import time
import streamlit as st

st.set_page_config(page_title='Minha Página', 
	page_icon='🔰', 
	layout="wide", 
	initial_sidebar_state="auto",
	menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    })

with st.spinner('Wait for it...'):
    time.sleep(1)

st.success('Done!')
st.info('Done!')
st.warning('Done!')
st.error('Done!')
 
 

if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')



st.divider()

if 'contagem' not in st.session_state:
    st.session_state['contagem'] = 0

def atualizar_contagem():
	st.session_state['contagem'] += 1

botao = st.button('Clique em mim', on_click = atualizar_contagem)

st.write(st.session_state)



st.divider()




with st.chat_message(name = 'user'):
	st.write('Oieeeee!')
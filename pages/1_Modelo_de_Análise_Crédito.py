import streamlit as st
import pickle
import pandas as pd
import math
from pathlib import Path

path_model = Path(__file__).parent.parent / "ml/analise_credito.pkl"

st.title('Executar Modelo')

with open (path_model,"rb") as arquivo:
    modelo = pickle.load(arquivo)
      
idade = math.ceil(st.number_input('Qual a sua Idade? ',format="%d"))
renda = st.number_input('Qual a sua Renda? ')
emprestimo = st.number_input('Qual o valor de empréstimo que deseja contratar? ')

data = {
    'person_age': [idade],
    'person_income': [renda],
    'loan_amnt': [emprestimo]
}

if st.button("Avaliar Aprovação de Crédito", key="clear", type="primary"):

    # Criar o DataFrame
    df = pd.DataFrame(data)
    df.reset_index(inplace = True)
    predictions = modelo.predict(X=df)
    if predictions[0] == 0:
        st.write(':green[Parabéns, crédito aprovado!]')
    else:
        st.write(':red[Seu crédito não foi aprovado!]')


import streamlit as st
import pickle
import pandas as pd
import math
from pathlib import Path

path_model = Path(__file__).parent.parent / "ml/analise_credito.pkl"
#path_model =  "..//ml//analise_credito.pkl"

st.title('Executar Modelo')

with open (path_model,"rb") as arquivo:
    modelo = pickle.load(arquivo)
    
    
idade = math.ceil(st.number_input('Qual a sua Idade? ',format="%d"))
st.write( idade)

renda = st.number_input('Qual a sua Renda? ')
st.write( renda)

emprestimo = st.number_input('Possui algum empréstimo? Qual o valor ')
st.write( emprestimo)


data = {
    'income': [renda],
    'age': [idade],
    'loan': [emprestimo]
}

if st.button("Avaliar Aprovação de Crédito", key="clear", type="primary"):

    # Criar o DataFrame
    df = pd.DataFrame(data)

    predictions = modelo.predict(X=df)
    st.write(predictions)


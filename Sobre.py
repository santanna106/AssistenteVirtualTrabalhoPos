import streamlit as st 


st.title('🏢 Análise de Crédito ')

st.header('Descrição do Aplicativo')
st.write(
    """
    A análise automática de crédito é uma prática fundamental no setor financeiro e tem uma grande importância
    devido a diversos motivos, que vão desde a eficiência operacional até a tomada de decisões mais precisas
    e justas. Possibilitando o processamento de grandes volumes de solicitações de crédito em tempo real, viabilizando
    uma resposta mais rápida para os clientes que solicitam empréstimos ou financimentos, 
    permitindo redução dos custos operacionais relacionados com a contratação de pessoal para avaliar as solicitações,
    tornando possível a personalização de ofertas baseadas no perfil dos clientes e 
    melhoria da experiência dos usuários dos serviços de uma instituição financeira em decorrência
    de uma análise mais rápida e assertiva. 
    """) 

st.write(
    """
    Com o objetivo de apresentar uma solução de automatização de análise de crédito. Este aplicativo implementa 
    um modelo de machine Learning que recebe como parâmetros
    a idade, renda e valor de empréstimo para realizar a análise de crédito e retornar se um determinado usuário
    terá o empréstimo aprovado ou não.
    """) 



st.subheader('Modelo de Análise de Crédito')

st.write(
    """
    Os dados utilizados para a criação do modelo foi adaptado do desafio kaggle
    https://www.kaggle.com/code/anshtanwar/credit-risk-prediction-training-and-eda .
    As features utilizadas para o desenvolvimento da solução foram: idade (person_age),
    renda(person_income) e valor solicitado para o empréstimo (loan_amnt).
 
    """) 
st.write("""
          A abordagem utilizada considerou  que classificar uma pessoa como
    boa pagadora quando na verdade ela é uma má pagadora traria um maior 
    custo para a instituição, ou seja, o Falso Negativo seria o pior erro 
    para o problema. 
    Já a classificação incorreta de um bom pagador traria um prejuízo 
    menor relacionado com a não realização de um negócio.
    Diante desta análise o recall foi a métrica mais importante 
    para avaliação do modelo.    
         """)

st.write("""
          O modelo com melhor adequação ao modelo foi a Árvore de Decisão. Ela
          apresentou o melhor recall.  
         """)

st.subheader('Equipe')

st.markdown("""
            <ul>
                <li>Gabriel Andrade de Sant'Anna</li>
                <li>João Freitas</li>
                <li>Midiã Silvane da Silva Marques</li>
            </ul>
""", unsafe_allow_html=True)


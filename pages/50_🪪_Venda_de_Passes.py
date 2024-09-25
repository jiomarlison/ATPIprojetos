from creditos import credito
import streamlit as st

st.set_page_config(
    page_title="Venda de Passes",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🪪"
)
st.title("COMPRA DE PASSES")
st.markdown(
    """
    Toda a venda de passe é feita em local adequado, geralmente em pontos de vendas especificos, 
    para estudantes é necessario estar com a carteira estudantil em mãos para realizar a compra, 
    para passes de funcionarios de empresas é necessario consultar o responsavel de cada empresa 
    para saber quais procedimentos são necessarios.
    """
)
st.title("CARTEIRA ESTUDANTIL")
st.markdown(
    """
    O estudante pode pedir a sua pela [internet](https://www.documentodoestudante.com.br/) 
    ou de forma presencial nas devidas organizações da cidade.\n

    """)
st.title("AVISOS")
st.markdown(
    """
    :blue[**OS ESTUDANTES DEVEM APRESENTAR SUA CARTEIRINHA ESTUDANTIL JUNTO A ENTREGA DO SEU PASSE AO MOTORISTA.**]\n
    :red[***OS PASSES DE ESTUDANTES SÃO DE USO UNICO DO ESTUDANTE, NÃO SENDO PERMITIDO REPASSAR A OUTRO INDIVIDUO,
    O ESTUDANTE QUE FOR PEGO PODERA SER IMPEDIDO DE REALIZAR A COMPRA DE NOVOS PASSES PELO PERIODO DE 1 ANO.***]
    """
)





credito()
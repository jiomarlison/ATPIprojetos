from creditos import credito
import streamlit as st
st.set_page_config(
    page_title="Inicio",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🔰"
)
# with st.sidebar:
#     st.markdown('''
#                 - [< 1 >](#1)
#                 - [< 2 >](#2)
#                 - [< 3 >](#3)
#                 - [< 4 >](#4)
#                 - [< 5 >](#5)
#                 - [< 6 >](#6)
#             ''', unsafe_allow_html=True)
# for x in range(1, 7):
#     st.header(f"{x}", anchor=f"{x}", divider='rainbow')
#     st.subheader(f":rainbow[{x}]")
#     st.subheader(f":rainbow[{x + 1}]")
#     st.subheader(f":rainbow[{x + 2}]")
#     st.header("", divider='rainbow')
st.header("Informações Básicas")
st.markdown(
    """
    Esta página foi feita com intuito de concentrar informações dos veículos que percorrem os projetos e outras regiões de petrolina, 
    reunindo em um só local informações de ***horários, valores, local de saida e mais*** de alguns dos transporte, 
    para então facilitar o acesso a essas informações para muito mais pessoas.
    """
)
st.markdown(":orange[Clique nos link abaixo para abrir uma nova aba com os horários de uma determinada empresa "
            "ou use o menu do lado esquerdo caso queira ficar nessa mesma página.]")
st.markdown("[ATPI_Projetos](/ATPI_Projetos)")
credito()
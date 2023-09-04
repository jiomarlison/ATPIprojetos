import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Ponto de Saida dos Transportes",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🚏"
)
st.title("Informações pontos de embarque para os Projetos")


@st.cache_data
def imagemPontoSaidaCentro():
    try:
        pontoSaidaCentro = Image.open("./Imagens/PontoCemiterio.png")
        return pontoSaidaCentro
    except:
        pontoSaidaCentro = Image.open("Imagens/PontoCemiterio.png")
        return pontoSaidaCentro


imagemPontoSaida = imagemPontoSaidaCentro()


@st.cache_data
def imagemPontoReferenciaCentro():
    try:
        pontoReferenciaCentro = Image.open("./Imagens/PlacaReferenciaPontos.png")
        return pontoReferenciaCentro
    except:
        pontoReferenciaCentro = Image.open("Imagens/PlacaReferenciaPontos.png")
        return pontoReferenciaCentro


imagemPontoSaidaRereferencia = imagemPontoReferenciaCentro()

st.subheader(
    """
    Centro de Petrolina - PE, em frente ao [Cemitério Central Campo Das Flores](https://goo.gl/maps/doB7CnkYnSDKHtz26)
    Aqui se concentram grande maioria dos carros com destino aos projetos entre outros localizações.
    Você pode se guiar de acordo com placas no local, indicando onde os carros de cada projeto param.
    Alem de que tais veículos apresentam em seu para-brisa e/ou laterais dos veículos placas e/ou escrituras que indicam
    a qual empresa pertencem e sua rota de percurso, quais projetos percorre
    No caso de duvida pode-se informar com pessoas do local, barracas de lanches ou até com os motoristas, caso tenha alguma duvida
    """,
    anchor="descricao_local",
    divider="blue"
)

placa, foto_local = st.columns(spec=[0.3, 0.7])
with placa:
    st.subheader("Essas Placas indicam o local onde o carro de cada local embarca")
    st.image(imagemPontoSaidaRereferencia)
with foto_local:
    st.subheader("Esse é um dos lados dos locais de embarque")
    st.markdown("##### Se reparar pode ver placas de diversas empresas para diversos locais")
    st.image(imagemPontoSaida)
st.divider()

from creditos import credito

credito()

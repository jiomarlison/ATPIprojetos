import streamlit as st
import datetime as dt
diasSemana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
@st.cache_data
def credito():
    st.sidebar.header("", divider="red")
    st.sidebar.header(":blue[O Site Ainda não foi totalmente construido, então ainda faltam informações a serem adicionadas]")
    st.sidebar.header("", divider="rainbow")
    st.sidebar.subheader(f":orange[DATA HOJE:] **{dt.datetime.now().strftime('%d/%m/%Y')}** - {diasSemana[dt.datetime.today().weekday()]}")




    st.sidebar.subheader('Site feito por [Jiomarlison Dias Souza](https://www.linkedin.com/in/jiomarlison-dias-souza)', divider="rainbow")

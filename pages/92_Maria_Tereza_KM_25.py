import streamlit as st
import pandas as pd
from datetime import *
from PIL import Image
from six import BytesIO

st.set_page_config(
    page_title="Horarios Maria Tereza KM-25",
    page_icon=":trolleybus:",
    layout='wide'
)

dias_horarios = ['SEGUNDA À SEXTA', 'SABADO', 'DOMINGO E FERIADOS']
sem = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")

if date.today().weekday() < 5:
    dia_hoje = dias_horarios[0]
elif date.today().weekday() == 5:
    dia_hoje = dias_horarios[1]
else:
    dia_hoje = dias_horarios[2]

st.markdown(f"# :scroll: HORÁRIOS DO PROJETO MARIA TEREZA KM-25")
st.markdown(f"##  Dia: {datetime.now().strftime('%d-%m-%Y')}(:green[{sem[date.today().weekday()]}])")

df = pd.read_excel(
    "COOPERTRANSERTÃO.xlsx",
    header=[1, 2, 3],
).fillna("")
colunas_dias = list(set([dias[0] for dias in df.columns]))[::-1]
colunas_dias.append("TODOS")
colunas_locais_saida = list(set([dias[1] for dias in df.columns]))
colunas_locais_saida.append("TODOS")


dia, local = st.columns(2)
with dia:
    st.subheader("📅 Selecione o dia do horario que deseja ver")
    selecao_dia = st.radio(
        label="📌 Selecione o dia que deseja ver",
        options=colunas_dias,
        horizontal=True,
        index=3
    )
    if selecao_dia is not "TODOS":
        df = df.loc[:, df.columns.get_level_values(0) == f"{selecao_dia}"]
with local:
    st.subheader("🔰 Selecione o local de saida para saber os horários")
    selecao_local = st.radio(
        label="📌 Selecione o local de saida",
        options=colunas_locais_saida,
        horizontal=True,
        index=2
    )
    if selecao_local is not "TODOS":
        df = df.loc[:, df.columns.get_level_values(1) == f"{selecao_local}"]

df = df.style.set_table_styles(
    [
        {"selector": "th", "props": [('text-align', 'center')]},
        {"selector": "td", "props": [('text-align', 'center')]},
        {"selector": "tbody td", "props": [("border", "2px solid black")]},
        {"selector": "th", "props": [("border", "2px solid black")]},
        {'selector': 'th:not(.index_name)',
         'props': 'background-color: #ADD8E6; color: black;'}
    ]
).hide(axis=0)

st.markdown(
    df.to_html(),
    unsafe_allow_html=True
)

try:
    horario_mariaTereza = Image.open("./Imagens/HORARIO - Projeto Maria Tereza KM-25.png")
except:
    horario_mariaTereza = Image.open("Imagens/HORARIO - Projeto Maria Tereza KM-25.png")

buffer = BytesIO()
horario_mariaTereza.save(buffer, format="PNG")

st.download_button(
    label="📁 Baixar Imagem do Horário Completo",
    data=buffer.getvalue(),
    file_name="HORARIO - Projeto Maria Tereza KM-25.png",
    mime="image/png",
)

from creditos import credito
credito()

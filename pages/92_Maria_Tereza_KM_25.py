import streamlit as st
import pandas as pd
import datetime as dt
from datetime import *
from collections import OrderedDict, defaultdict

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

st.markdown("# :scroll: TABELA DE HORÁRIOS DO PROJETO MARIA TEREZA")
st.markdown(f"##  Dia: :green[{sem[date.today().weekday()]}]")

st.title(
    ":date: **Selecione ou remova os dias dos horarios que deseja ver**",
    help=":green[**Selecione Segunda á Sexta para ver os horários desses dias**]"
)
dias_horarios_selecionados = st.multiselect(
    "# :pushpin: **Selecione o(s) dia(s) que deseja ver**",
    options=dias_horarios,
    default=dia_hoje
)
if len(dias_horarios_selecionados) == 0:
    st.warning("Selecione ao menos 1 dia")
st.title(
    ":beginner: **Selecione ou remova o local de saida para saber os horários**",
    help=":green[Do **KM-25** a **Petrolina** selecione **KM-25**,"
         " do **Petrolina** para **KM-25** selecione **Petrolina**]",
)
local_saida = st.multiselect(
    "# :busstop: **Ponto de Saida**",
    options=["KM-25", "Petrolina"],
    default=["KM-25", "Petrolina"],
    disabled=len(dias_horarios_selecionados) == 0
)
cabecalho_horarios = pd.MultiIndex.from_product(
    [
        ["Horário Proj. Maria Tereza KM-25"],
        dias_horarios_selecionados,
        local_saida,
        ["Veiculo", "Horário", "Área"]
    ]
)
horario_segunda_sexta = pd.DataFrame(columns=cabecalho_horarios)

if dias_horarios_selecionados is not None:
    if 'SEGUNDA À SEXTA' in dias_horarios_selecionados:
        if 'KM-25' in local_saida:
            horario_segunda_sexta["Horário Proj. Maria Tereza KM-25", 'SEGUNDA À SEXTA', 'KM-25', "Veiculo"] = \
                [
                    "", "1º", "2º", "4º", "8º", "6º", "7º", "3º", "1º", "2º", "8º",
                    "3º", "7º", "4º", "1º", "6º", "2º", "8º", "7º", "6º", "3º",
                ]
            horario_segunda_sexta["Horário Proj. Maria Tereza KM-25", 'SEGUNDA À SEXTA', 'KM-25', "Horário"] = \
                [
                    "", "05:50", "06:20", "06:45", "07:00", "07:10", "07:30", "08:00", "08:45", "09:30", "10:15",
                    "11:15", "12:00", "12:45", "13:30", "14:30", "15:50", "16:30", "17:00", "17:25", "18:10",
                ]
            horario_segunda_sexta["Horário Proj. Maria Tereza KM-25", 'SEGUNDA À SEXTA', 'KM-25', "Área"] = \
                [
                    "", "VILA", "VILA", "A-20", "19/22", "R-4", "R-5/21", "VILA", "VILA", "VILA", "VILA",
                    "VILA", "R-4", "VILA", "VILA", "VILA", "VILA", "19/22", "R-5", "R-4", "VILA",
                ]
        if 'Petrolina' in local_saida:
            horario_segunda_sexta["Horário Proj. Maria Tereza KM-25", 'SEGUNDA À SEXTA', 'Petrolina', "Veiculo"] = \
                [
                    "TODOS", "3º", "1º", "2º", "8º", "3º", "7º", "4º", "1º", "6º", "2º",
                    "8º", "7º", "4º", "6º", "3º", "1º", "2º", "8º", "", "",
                ]
            horario_segunda_sexta["Horário Proj. Maria Tereza KM-25", 'SEGUNDA À SEXTA', 'Petrolina', "Horário"] = \
                [
                    "05:20", "06:10", "07:10", "08:00", "09:00", "09:45", "10:30", "11:15", "12:00", "12:30",
                    "13:10", "13:50", "14:30", "15:10", "15:50", "16:30", "17:00", "18:15", "22:00", "", "",
                ]
            horario_segunda_sexta["Horário Proj. Maria Tereza KM-25", 'SEGUNDA À SEXTA', 'Petrolina', "Área"] = \
                [
                    "TODOS", "VILA", "VILA", "VILA", "VILA", "VILA", "R-4", "VILA", "VILA", "R-4/21",
                    "VILA", "19/22", "R-5", "20", "R-4", "VILA", "VILA", "VILA", "ALUNO", "", "",
                ]
        st.markdown(horario_segunda_sexta.to_html(), unsafe_allow_html=True)
        st.divider()
        st.title(":checkered_flag: Filtar Por Destino")
        filtroDestino = st.radio(
            "Selecione o destino",
            options=
            set(
                horario_segunda_sexta["Horário Proj. Maria Tereza KM-25", 'SEGUNDA À SEXTA', 'Petrolina', "Área"]
            )
            ,
            horizontal=True
        )
        st.write(
            pd.DataFrame(horario_segunda_sexta["Horário Proj. Maria Tereza KM-25", 'SEGUNDA À SEXTA'].loc[
                             horario_segunda_sexta[
                                 "Horário Proj. Maria Tereza KM-25", 'SEGUNDA À SEXTA', 'Petrolina' or "KM-25", "Área"]
                             == filtroDestino
                             ]).to_html(),
            unsafe_allow_html=True
        )
        st.divider()
from creditos import credito
credito()

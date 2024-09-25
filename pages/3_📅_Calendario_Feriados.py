import streamlit as st
import pandas as pd
from datetime import *

st.set_page_config(
    page_title="Calendario de Feriados",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📅"
)

ano_atual = datetime.today().year
mes_atual = datetime.today().month
dia_atual = datetime.today().day
lista_meses = ['Janeiro', 'Fevereiro', 'Março',
               'Abril', 'Maio', 'Junho',
               'Julho', 'Agosto', 'Setembro',
               'Outubro', 'Novembro', 'Dezembro']
lista_dias_semana = ['Domingo', "Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado"]

cal_feriados = pd.DataFrame(
    {
        "Data": pd.date_range(
            f'{ano_atual}-01-01',
            f'{ano_atual}-12-31',
            freq='d'
        ).strftime("%d/%m/%Y")
    }
)
cal_feriados['Dia da Semana'] = [datetime.strptime(x, '%d/%m/%Y').strftime("%A") for x in
                                 cal_feriados['Data']]
cal_feriados["Feriado"] = ''
cal_feriados['Mês'] = [datetime.strptime(x, '%d/%m/%Y').strftime("%B") for x in cal_feriados['Data']]

cal_feriados = cal_feriados.replace(
    ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
    lista_dias_semana
).replace(
    ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
     'December'],
    lista_meses
)
cal_feriados["Feriado"].loc[cal_feriados['Data'] == f'01/01/{ano_atual}'] = "Confraternização Universal"
cal_feriados["Feriado"].loc[cal_feriados['Data'] == f'21/02/{ano_atual}'] = "Carnaval"
cal_feriados["Feriado"].loc[cal_feriados['Data'] == f'06/03/{ano_atual}'] = "Revolução Pernambucana"
cal_feriados["Feriado"].loc[cal_feriados['Data'] == f'21/04/{ano_atual}'] = "Tiradentes"
cal_feriados["Feriado"].loc[cal_feriados['Data'] == f'01/05/{ano_atual}'] = "Dia do Trabalho"
cal_feriados["Feriado"].loc[cal_feriados['Data'] == f'24/06/{ano_atual}'] = "Dia de São João"
cal_feriados["Feriado"].loc[cal_feriados['Data'] == f'15/08/{ano_atual}'] = "Nossa Senhora Rainha dos Anjos"

cal_feriados["Feriado"].loc[cal_feriados['Data'] == f'07/09/{ano_atual}'] = "Independencia do Brasil"
cal_feriados["Feriado"].loc[cal_feriados['Data'] == f'21/09/{ano_atual}'] = "Aniversario da Cidade"

cal_feriados["Feriado"].loc[cal_feriados['Data'] == f'12/10/{ano_atual}'] = "Nossa Senhora Aparecida"
cal_feriados["Feriado"].loc[cal_feriados['Data'] == f'02/11/{ano_atual}'] = "Finados"
cal_feriados["Feriado"].loc[cal_feriados['Data'] == f'15/11/{ano_atual}'] = "Proclamação da Republica"
cal_feriados["Feriado"].loc[cal_feriados['Data'] == f'25/12/{ano_atual}'] = "Natal"

cal_feriados = cal_feriados

lista_datas_feriados = pd.DataFrame(cal_feriados.loc[cal_feriados['Feriado'] != ""]).to_dict(orient='records')
lista = []
for x, y in enumerate(lista_datas_feriados):
    lista.append([lista_datas_feriados[x]["Data"], lista_datas_feriados[x]["Feriado"]])
if f'{dia_atual}/{mes_atual}{ano_atual}]' in lista:
    st.subheader(
        f"Data: :blue[{dia_atual}] de :red[{lista_meses[mes_atual - 1]}] de :green[{ano_atual}], :orange[*Horário de Feriado*]")
    st.dataframe(data=cal_feriados.loc[cal_feriados['Data'] == f"{dia_atual}/{mes_atual}{ano_atual}"], use_container_width=True, hide_index=True)
else:
    st.subheader(
        f"Data: :blue[{dia_atual}]"
        f" de :red[{lista_meses[mes_atual - 1]}]"
        f" de :green[{ano_atual}],"
        f" Horário de :orange[*{lista_dias_semana[datetime.today().weekday() + 1]}*]")

with st.expander("Lista dos Feriados", expanded=False):
    st.dataframe(
        cal_feriados.loc[cal_feriados['Feriado'] != ""],
        use_container_width=True,
        hide_index=True,
    )
with st.expander("Filtrar Feriados por Mês"):
    st.radio("Filtrar por mês", options=cal_feriados['Mês'].unique(), key='mes_selecionado', horizontal=True,
             index=mes_atual - 1)
    st.dataframe(
        cal_feriados.loc[cal_feriados["Mês"] == st.session_state.mes_selecionado],
        use_container_width=True,
        hide_index=True,
    )

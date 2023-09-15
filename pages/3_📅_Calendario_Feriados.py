import datetime

import streamlit as st
import pandas as pd
import sqlite3
from datetime import *
st.set_page_config(
    page_title="Calendario de Feriados",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📅"
)
# conexao = sqlite3.connect("Feriados.db")
ano_atual = datetime.today().year
mes_atual = datetime.today().month
dia_atual = datetime.today().day
lista_meses = ['Janeiro', 'Fevereiro', 'Março',
               'Abril', 'Maio', 'Junho',
               'Julho', 'Agosto', 'Setembro',
               'Outubro', 'Novembro', 'Dezembro']
lista_dias_semana = ['Domingo', "Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado"]


# with st.expander("Conteudo Banco"):
#     try:
#         tabela_feriado_banco = st.data_editor(
#             pd.read_sql("SELECT * FROM feriados", conexao),
#             column_config={
#                 "ID": st.column_config.NumberColumn(disabled=True),
#                 "Data": st.column_config.TextColumn(disabled=True),
#                 'Dia da Semana': st.column_config.TextColumn(disabled=True),
#                 'Mês': st.column_config.TextColumn(disabled=True)
#
#             },
#             use_container_width=True,
#             hide_index=True
#         )
#     except:
#         st.write("Naõ foi")

calendario_feriados = pd.DataFrame(
    {
        "Data": pd.date_range(
            f'{ano_atual}-01-01',
            f'{ano_atual}-12-31',
            freq='d'
        ).strftime("%d/%m/%Y")
    }
)
calendario_feriados['Dia da Semana'] = [datetime.strptime(x, '%d/%m/%Y').strftime("%A") for x in
                                        calendario_feriados['Data']]
calendario_feriados["Feriado"] = ''
calendario_feriados['Mês'] = [datetime.strptime(x, '%d/%m/%Y').strftime("%B") for x in calendario_feriados['Data']]

calendario_feriados = calendario_feriados.replace(
    ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
    lista_dias_semana
).replace(
    ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
     'December'],
    lista_meses
)
calendario_feriados["Feriado"].loc[calendario_feriados['Data'] == f'01/01/{ano_atual}'] = "Confraternização Universal"
calendario_feriados["Feriado"].loc[calendario_feriados['Data'] == f'21/02/{ano_atual}'] = "Carnaval"
calendario_feriados["Feriado"].loc[calendario_feriados['Data'] == f'06/03/{ano_atual}'] = "Revolução Pernambucana"
calendario_feriados["Feriado"].loc[calendario_feriados['Data'] == f'21/04/{ano_atual}'] = "Tiradentes"
calendario_feriados["Feriado"].loc[calendario_feriados['Data'] == f'01/05/{ano_atual}'] = "Dia do Trabalho"
calendario_feriados["Feriado"].loc[calendario_feriados['Data'] == f'24/06/{ano_atual}'] = "Dia de São João"
calendario_feriados["Feriado"].loc[calendario_feriados['Data'] == f'15/08/{ano_atual}'] = "Nossa Senhora Rainha dos Anjos"

calendario_feriados["Feriado"].loc[calendario_feriados['Data'] == f'07/09/{ano_atual}'] = "Independencia do Brasil"
calendario_feriados["Feriado"].loc[calendario_feriados['Data'] == f'21/09/{ano_atual}'] = "Aniversario da Cidade"

calendario_feriados["Feriado"].loc[calendario_feriados['Data'] == f'12/10/{ano_atual}'] = "Nossa Senhora Aparecida"
calendario_feriados["Feriado"].loc[calendario_feriados['Data'] == f'02/11/{ano_atual}'] = "Finados"
calendario_feriados["Feriado"].loc[calendario_feriados['Data'] == f'15/11/{ano_atual}'] = "Proclamação da Republica"
calendario_feriados["Feriado"].loc[calendario_feriados['Data'] == f'25/12/{ano_atual}'] = "Natal"

calendario_feriados = calendario_feriados
# def criar_banco_feriados(tabela, conexao_banco):
#     tabela.to_sql(
#         name="feriados",
#         con=conexao_banco,
#         if_exists='replace',
#     )
#
#
# banco_de_dados_feriados = criar_banco_feriados(calendario_feriados, conexao)

lista_datas_feriados = pd.DataFrame(calendario_feriados.loc[calendario_feriados['Feriado'] != ""]).to_dict(orient='records')
lista = []
for x, y in enumerate(lista_datas_feriados):
    lista.append([lista_datas_feriados[x]["Data"], lista_datas_feriados[x]["Feriado"]])
if f'{dia_atual}/{mes_atual}{ano_atual}]' not in lista:
    st.subheader(
        f"Data: :blue[{dia_atual}] de :red[{lista_meses[mes_atual - 1]}] de :green[{ano_atual}], :orange[*Horário de Feriado*]")
    st.dataframe(data=calendario_feriados.loc[calendario_feriados['Data'] == f"{dia_atual}/{mes_atual}{ano_atual}"], use_container_width=True, hide_index=True)
else:
    st.subheader(
        f"Data: :blue[{dia_atual}]"
        f" de :red[{lista_meses[mes_atual - 1]}]"
        f" de :green[{ano_atual}],"
        f" Horário de :orange[*{lista_dias_semana[datetime.today().weekday() + 1]}*]")

with st.expander("Lista dos Feriados", expanded=False):
    st.dataframe(
        calendario_feriados.loc[calendario_feriados['Feriado'] != ""],
        use_container_width=True,
        hide_index=True,
    )
with st.expander("Filtrar Feriados por Mês"):
    st.radio("Filtrar por mês", options=calendario_feriados['Mês'].unique(), key='mes_selecionado', horizontal=True,
             index=mes_atual - 1)
    st.dataframe(
        calendario_feriados.loc[calendario_feriados["Mês"] == st.session_state.mes_selecionado],
        use_container_width=True,
        hide_index=True,
    )

# st.button("Cria Banco de Dados dos Feriados", on_click=banco_de_dados_feriados)
# conexao.close()
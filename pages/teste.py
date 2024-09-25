import datetime

import pandas as pd
import streamlit as st
import dataframe_image as dfi
from io import BytesIO
from creditos import credito

df = pd.read_excel(
    "COOPERTRANSERTÃO.xlsx",
    header=[0, 1, 2, 3],
).fillna("")

df = df.rename(
    columns={
        "TABELA DE HORÁRIOS DO PROJETO MARIA TEREZA KM-25"
        :
        f"HORÁRIOS DO PROJETO MARIA TEREZA KM_25 - {datetime.datetime.now().strftime('%d-%m-%Y')}"
    }
)

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



buffer = BytesIO()
# dfi.export(df, buffer, dpi=500)
dfi.export(df, buffer)
st.image(buffer.getvalue())
st.download_button(
    label="Baixar Horário",
    data=buffer.getvalue(),
    file_name="Projeto Maria Tereza KM-25.png"
)

credito()
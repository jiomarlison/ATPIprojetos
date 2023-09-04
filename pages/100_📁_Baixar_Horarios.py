import pandas as pd
from io import BytesIO
import streamlit as st

st.set_page_config(
    page_title="Baixar Horários",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📁"
)

st.markdown("# :blue[Horários Completo ATPI Projetos]")


@st.cache_data
def horario():
    tabela_horario = pd.DataFrame(
        columns=["Horário_1", "Rota_1", "Horário_2", "Rota_2", "Horário_3", "Rota_3", "Horário_4", "Rota_4"],
        index=[f'{x}º' for x in range(1, 23)]
    )

    def preencher(lista: list):
        if len(lista) < 22:
            for x in range(22 - len(lista)):
                lista.append('')
        return lista

    tabela_horario['Horário_1'] = preencher([
        "05:45",
        "05:50",
        "06:10",
        "06:30",
        "07:00",
        "08:10",
        "09:10",
        "10:10",
        "11:00",
        "12:00",
        "13:00",
        "14:00",
        "15:00",
        "16:00",
        "17:00",
        "18:10",
        "19:10",
        "22:10"

    ])
    tabela_horario['Rota_1'] = preencher([
        "Saída N1",
        "Via N2",
        "(Carro Reserva) - Saída de Tulio - N1 para à cidade",
        "",
        "",
        "Via N2",
        "",
        "Via N2",
        "",
        "Via N2",
        "",
        "",
        "Via N2",
        "",
        "",
        "Via N2, encerra no N3",
        "Via N2",
        "19:10 - Via N2 Saindo da faculdade(FACAPE)"
    ])
    tabela_horario["Horário_2"] = preencher([
        "06:00",
        "06:00",
        "07:00",
        "08:00",
        "08:30",
        "09:30",
        "10:30",
        "11:50",
        "12:50",
        "13:30",
        "14:30",
        "15:30",
        "16:30",
        "18:00",

    ])
    tabela_horario["Rota_2"] = preencher([
        "Saída N1",
        "Via N2",
        "",
        "",
        "Via N2",
        "",
        "",
        "",
        "",
        "",
        "Via N2",
        "",
        "",
        "Via N2",

    ])
    tabela_horario["Horário_3"] = preencher([
        "06:00",
        "09:00",
        "12:00",
        "15:00",
        "18:00",

    ])
    tabela_horario["Rota_3"] = preencher([
        "Via N2 ( Volta feira Ouro Preto)",
        "Feira Ouro Preto (Ida/Volta)",
        "Via N2( Ida/Volta)",
        "",
        "Via N2"
    ])
    tabela_horario["Horário_4"] = preencher([
        "06:00",
        "09:00",
        "12:00",
        "15:00",
        "18:00",

    ])
    tabela_horario["Rota_4"] = preencher([
        "Via N2",
        "",
        "Via N2",
        "",
        "Via N2"
    ])

    return tabela_horario


horario_completo = horario()
horario_completo.columns = pd.MultiIndex.from_product(
    [["Segunda à Sexta", "Sabado", "Domingo", "Feriado"], ["Horário", "Rota"]]
)

st.write(horario_completo.to_html(), unsafe_allow_html=True)
st.divider()


@st.cache_data
def baixarPlanilha(df, index=True):
    df.dropna()
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine="xlsxwriter")
    df.to_excel(writer, index=index, sheet_name="Sheet1")
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0'})
    worksheet.set_column('A:A', None, format1)
    writer.close()
    processed_data = output.getvalue()
    return processed_data


tabela_horario_completo = baixarPlanilha(horario_completo)
st.header("Baixar Arquivo Aqui", anchor="baixar_arquivo")
st.download_button(label="📥 :red[Baixar Planilha Todos Horários]", data=tabela_horario_completo,
                   file_name='Horário ATPI Transporte.xlsx')


from creditos import credito
credito()

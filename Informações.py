import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(
    page_title="Registro de Horarios",
    layout="wide",
    initial_sidebar_state="expanded"
)


def modificar_horario():
    conexao = sqlite3.connect("ATPI.db")
    cursor = conexao.cursor()

    with st.expander("Modificações Horários"):
        try:
            horario_ATPI = pd.read_sql(
                sql=f'''
                    SELECT * FROM horario_ATPI
                ''',
                con=conexao
            )
        except:
            horario_ATPI = pd.DataFrame(
                columns=["Dia", "Horário", "Rota", "Descriçao"]
            )
            horario_ATPI.to_sql(
                name=f"horario_ATPI",
                con=conexao,
                if_exists="append",
                index=True
            )
        horario_ATPI_streamlit = st.data_editor(
            data=horario_ATPI,
            num_rows="dynamic",
            use_container_width=True,
        )

        def enviar_horario_ATPI_para_banco(horario):
            horario.to_sql(
                name=f"horario_ATPI",
                con=conexao,
                if_exists="replace",
                index=True
            )

        # aviso_registro_horario = st.toast("Horario ATPI registrado")
        registra_horario_ATPI = st.button(
            label="Registrar horario no banco de dados"
        )
        if registra_horario_ATPI:
            enviar_horario_ATPI_para_banco(horario_ATPI_streamlit)
        cursor.close()
        conexao.close()


def horarios():
    conexao = sqlite3.connect("ATPI.db")
    cursor = conexao.cursor()
    try:
        horario_ATPI = pd.read_sql(
            sql=f'SELECT * FROM horario_ATPI',
            con=conexao
        )
        st.header("Selecione o Horário que deseja ver")
        horarios_disponiveis = horario_ATPI['Dia'].unique()
        for horario in horarios_disponiveis:
            with st.expander(f"Horários {horario}"):
                st.dataframe(
                    horario_ATPI.loc[horario_ATPI["Dia"] == horario],
                    use_container_width=True,
                    hide_index=True
                )
        st.header("Todos os Horários")
        with st.expander(":red[Todos os Horários]"):
            st.dataframe(
                horario_ATPI,
                use_container_width=True,
                hide_index=True,

            )
    except:
        st.error("Não foi possivel abrir os horários")

    cursor.close()
    conexao.close()


horarios()

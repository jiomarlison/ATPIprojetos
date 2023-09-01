import pandas as pd
import streamlit as st
from PIL import Image
import datetime as dt

try:
    logoATPI = Image.open("Imagens/Logo ATPI 1.jpg")
except:
    logoATPI = Image.open("./Imagens/Logo ATPI 1.jpg")
try:
    pontoSaidaCentro = Image.open("Imagens/CemiterioMunicipal.png")
except:
    pontoSaidaCentro = Image.open("./Imagens/CemiterioMunicipal.png")

diasSemana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
st.set_page_config(
    page_title="ATPI Projetos",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.sidebar.markdown(":red[**Feito Por**]")
st.sidebar.markdown("[jiomarlison D. Souza](https://www.linkedin.com/in/jiomarlison-dias-souza/)")

st.markdown("# **HORÁRIOS** VIA C1, N1, N2, N3")
st.markdown(f"## DATA HOJE: **{dt.datetime.now().strftime('%d/%m/%Y')}** - {diasSemana[dt.datetime.today().weekday()]}")

horarios, localizacao, identificacao, preco = st.tabs(
    [
        ":red[**Horário**]",
        ":blue[**Localização**]",
        ":red[**Identificação dos Carros**]",
        ":blue[**Preço**]"

    ]
)
with horarios:
    segunda_sexta, sabado, domingo, feriados, teste = st.columns(5)

    with segunda_sexta:
        st.markdown("# Segunda à Sexta")


        @st.cache_data
        def carregar_horarios_segunda_sexta():
            return pd.DataFrame(
                columns=["Horário", "Rota"], data={
                    "Horário": [
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
                    ],
                    'Rota': [
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
                    ]
                }
            )


        horario_segunda_sexta = carregar_horarios_segunda_sexta()
        horario_segunda_sexta["Horário"] = pd.to_datetime(horario_segunda_sexta["Horário"], format="%H:%M").dt.time
        # st.dataframe(
        #     horario_segunda_sexta,
        #     use_container_width=True,
        #     hide_index=True,
        # )
        st.table(horario_segunda_sexta.style.set_properties(
            **{'background-color': 'white',
               'color': 'red',
               }
        ),
        )

    with sabado:
        st.markdown("# Sábado")


        @st.cache_data
        def carregar_horarios_sabado():
            return pd.DataFrame(
                columns=["Horário", "Rota"], data={
                    "Horário": [
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

                    ],
                    'Rota': [
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

                    ]
                }
            )


        horarios_sabado = carregar_horarios_sabado()
        horarios_sabado["Horário"] = pd.to_datetime(horarios_sabado["Horário"], format="%H:%M").dt.time
        # st.dataframe(
        #     horarios_sabado,
        #     use_container_width=True,
        #     hide_index=True
        # )
        st.table(horarios_sabado.style.set_properties(
            **{'background-color': 'white',
               'color': 'green',
               }
        ),
        )

    with domingo:
        st.markdown("# Domingo")


        @st.cache_data
        def carregar_horarios_domingo():
            return pd.DataFrame(
                columns=["Horário", "Rota"], data={
                    "Horário": [
                        "06:00",
                        "09:00",
                        "12:00",
                        "15:00",
                        "18:00",

                    ],
                    'Rota': [
                        "Via N2 ( Volta feira Ouro Preto)",
                        "Feira Ouro Preto (Ida/Volta)",
                        "Via N2( Ida/Volta)",
                        "",
                        "Via N2"
                    ]
                }
            )


        horarios_domingo = carregar_horarios_domingo()
        horarios_domingo["Horário"] = pd.to_datetime(horarios_domingo["Horário"], format="%H:%M").dt.time
        # st.dataframe(
        #     horarios_domingo,
        #     use_container_width=True,
        #     hide_index=True
        # )
        st.table(
            horarios_domingo.style.set_properties(
                **{'background-color': 'white',
                   'color': 'Blue',
                   }
            )
        )

    with feriados:
        st.markdown("# Feriados")


        @st.cache_data
        def carregar_horarios_feriados():
            return pd.DataFrame(
                columns=["Horário", "Rota"], data={
                    "Horário": [
                        "06:00",
                        "09:00",
                        "12:00",
                        "15:00",
                        "18:00",

                    ],
                    'Rota': [
                        "Via N2",
                        "",
                        "Via N2",
                        "",
                        "Via N2"
                    ]
                }
            )


        horarios_feriados = carregar_horarios_feriados()
        horarios_feriados["Horário"] = pd.to_datetime(horarios_feriados["Horário"], format="%H:%M").dt.time
        # st.dataframe(
        #     horarios_domingo,
        #     use_container_width=True,
        #     hide_index=True
        # )
        st.table(
            horarios_feriados.style.set_properties(
                **{'background-color': 'white',
                   'color': 'teal',
                   }
            )
        )

with localizacao:
    st.title("LOCALIZAÇÃO")
    st.subheader(
        "Ponto de saída: Centro de Petrolina - PE, em frente ao [Cemitério Central Campo Das Flores](https://goo.gl/maps/doB7CnkYnSDKHtz26)")
    st.image(pontoSaidaCentro)

with identificacao:
    st.markdown("# COMO IDENTIFICAR OS CARROS DO PROJETO")
    st.image(logoATPI)
    st.markdown("#### Todos os carros devem mostrar no para-brisa quais os projetos que ele percorre,"
                " além de apresentar na lateral uma placa que identifica a empresa do carro e os projetos.")
    st.markdown("#### No caso de duvida pode-se perguntar ao motorista do carro.")

with preco:
    st.markdown("# TABELA DE PREÇOS")
    st.markdown("#### Seguindo DECRETO Nº 007/2023 da prefeitura de Petrolina estabelece"
                " o valor da tarifa do transporte coletivo urbano de passageiros no valor"
                " de R$ 8,00 da ATPI nos Projetos N1, N2, N3 e C1. Confira o decreto "
                "[AQUI](https://petrolina.pe.gov.br/wp-content/uploads/2023/02/decreto-007.pdf)")
st.sidebar.markdown("[Projeto Maria Tereza KM-25](projetomariatereza.streamlit.app)")

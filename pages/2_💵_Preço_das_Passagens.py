import streamlit as st

st.set_page_config(
    page_title="Preço Passagens",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="💵"
)

st.title("PREÇOS")
st.markdown(
    """
    O preço padrão da passagem é definido via decreto da preitura  de Petrolina- PE,
    onde passagens entre projetos ou rotas alternativas ficam a cargo de das propiás empresas definirem,
    você pode conferir o decreto da prefeitura para saber os preços decretado por ela para cada linha(empresa/rota) clicando
    [AQUI](https://petrolina.pe.gov.br/wp-content/uploads/2023/02/decreto-007.pdf).
    """
)

















from creditos import credito
credito()
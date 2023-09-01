import pandas as pd
import streamlit
import streamlit as st
from datetime import time

with st.sidebar:
    st.markdown('''
                - [< 1 >](#1) 
                - [< 2 >](#2) 
                - [< 3 >](#3) 
                - [< 4 >](#4) 
                - [< 5 >](#5) 
                - [< 6 >](#6) 
            ''', unsafe_allow_html=True)
for x in range(1, 7):
    st.header(f"{x}", anchor=f"{x}", divider='rainbow')
    st.subheader(f":rainbow[{x}]")
    st.subheader(f":rainbow[{x + 1}]")
    st.subheader(f":rainbow[{x + 2}]")
    st.header("", divider='rainbow')

st.caption('Site feito por [Jiomarlison Dias Souza](https://wa.me/5587981491787)')
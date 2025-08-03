import streamlit as st  
import pandas as pd

dados = pd.read_excel('bd_vendas.xlsx')
print(dados.head())


st.title('Ola, tudo bem?')

nome = st.text_input('Digite seu nome : ')

if nome:
    st.text(f' Seja bem vindo {nome}')


st.data_editor(dados)










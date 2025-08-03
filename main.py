import pandas as pd
import streamlit as st 

dados = pd.read_excel('bd_vendas.xlsx')

st.text('Olá , seja bem vindo')

st.text('Tabela de produtos')
botao = st.button('Clique aqui')

if botao:
    st.data_editor(dados)



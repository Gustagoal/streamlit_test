import pandas as pd
import streamlit as st 

dados = pd.read_excel('bd_vendas.xlsx')

st.text('Olá , seja bem vindo')

st.text('Tabela de produtos')

planilha = st.data_editor(dados)

st.download_button(
    label='📥 Baixar tabela editada',
    data='excel_bytes',
    file_name='planilha_editada.xlsx',
    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
)



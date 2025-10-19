import streamlit as st 
import pandas as pd 

with st.sidebar:
    upload = st.file_uploader("Insira seu arquivo")
    if upload:
     st.success("Arquivo inserido com sucesso")

    df = pd.read_excel(upload)
    st.radio(label="Selecione as opções abaixo",options=df['Categoria'].unique())


st.subheader("Planilha de custos")
st.bar_chart(df,x= "Nome_Produto", y= "Preco_Unit")
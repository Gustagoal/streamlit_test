import streamlit as st 
import pandas as pd 

with st.sidebar:
    try:
        upload = st.file_uploader("Insira seu arquivo")
        st.success("Arquivo carregado com sucesso")
    except Exception as e:
        st.text("Insira um arquivo")
    df = pd.read_excel(upload)
    st.radio(label="Selecione as opções abaixo",options=df['Categoria'].unique())


st.subheader("Planilha de custos")
st.bar_chart(df,x= "Nome_Produto", y= "Preco_Unit")
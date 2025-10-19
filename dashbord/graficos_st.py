import streamlit as st 
import pandas as pd 


df = pd.read_excel(r"C:\Users\Gustavo Castro\Desktop\streamlit_test\dashbord\planilha_unica.xlsx")


st.title("Olá seja bem vindo")
st.data_editor(df)
st.bar_chart(df["Categoria"])


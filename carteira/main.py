import pandas as pd
import streamlit as st

carteira = {
    "itau":[100],
    "nubank":[85]
}

df = pd.DataFrame(carteira)
df.to_excel("carteira.xlsx")


if st.sidebar:
    st.text("Controle de gastos")
st.text(f'Seu saldo no Itau é {df["itau"].unique()}R$')
st.text(f'Seu saldo no Nubank é {df["nubank"].unique()}R$')

adicionar = st.number_input("Digite um valor que deseja adicionar")

if adicionar:
    df["itau"] += adicionar
    st.text(f"Valor atualizado do itau {df["itau"].unique()} R$")


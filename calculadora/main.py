import streamlit as st 

with st.sidebar:
    st.title("Calculadora de IMC")
    st.image(r"C:\Users\Gustavo Castro\Desktop\streamlit_test\calculadora\obesidade.jpg")

peso = st.number_input(label= "Digite seu peso ",min_value=0.0)
altura = st.number_input(label = "Digite sua altura",min_value=0.0)

botao = st.button("Calcular")

if botao:
    imc = peso/(altura**2)
    if imc<18.5:
        st.warning("Abaixo do peso")
    elif imc >= 18.5 and imc <=24.9 :
        st.text("Peso Normal")
    elif imc >= 25 and imc <=29.9:
        st.text("Excesso de peso")
    elif imc >= 30 and imc <=34.9  :
        st.text("Obsidade")
    elif imc >= 35:
        st.warning("EXTREMA Obsidade",icon="🟥")
        
    st.text(f"O calculo de IMC é de {round(imc,2)}")

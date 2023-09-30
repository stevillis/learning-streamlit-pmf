import time

import streamlit as st

st.title("Funções de Layout")

st.sidebar.title("st.sidebar")
st.sidebar.image("stevillis_logo.png", width=120)

operation = st.sidebar.radio(
    "Escolha a operação", ["Adição", "Subtração", "Multiplicação", "Divisão"]
)

st.header("Calculadora")

num1 = st.number_input("Primeiro Número")
num2 = st.number_input("Segundo Número")

if operation == "Adição":
    st.write("Resultado:", num1 + num2)
if operation == "Subtração":
    st.write("Resultado:", num1 - num2)
if operation == "Multiplicação":
    st.write("Resultado:", num1 * num2)
if operation == "Divisão":
    st.write("Resultado:", num1 / num2)


st.markdown("---")
st.header("st.expander()")

with st.expander("Ajuda"):
    st.write(
        "Informe Primeiro e Segundo Número e veja o resultado da operação escolhida."
    )

with st.expander("Quadrado"):
    numero3 = st.number_input("Informe um Número")
    st.write("Quadrado de", numero3, "é:", numero3 * numero3)

st.markdown("---")
st.header("st.container()")

st.subheader("Concatenar Nomes")

primeiro_nome = st.text_input("Primeiro Nome:")
container = st.container()
ultimo_nome = st.text_input("Último Nome:")

incluir_meio = st.checkbox("Incluir o nome do meio?")
nome_meio = ""
if incluir_meio:
    nome_meio = container.text_input("Nome do Meio:")

st.write("Nome Completo:", primeiro_nome, nome_meio, ultimo_nome)

st.markdown("---")
st.header("st.empty()")

st.subheader("Contador sem st.empty()")

for segundos in range(10):
    st.write("Contagem:", segundos + 1)
    time.sleep(0.2)

st.subheader("Contador com st.empty()")
contador = st.empty()
with contador:
    for segundos in range(10):
        st.write("Contagem:", segundos + 1)
        time.sleep(0.2)

st.markdown("---")
st.header("st.columns()")

st.subheader("Colunas com tamanhos iguais")
col1, col2, col3 = st.columns(3)

with col1:
    numero1 = st.number_input("Número 1")
    check1 = st.checkbox("Check 1")

with col2:
    numero2 = st.number_input("Número 2")
    check2 = st.checkbox("Check 2")

with col3:
    numero3 = st.number_input("Número 3")

st.subheader("Colunas com tamanhos diferentes")
cola, colb, colc = st.columns([1, 2, 1])

with cola:
    numeroa = st.number_input("Número a")
    checka = st.checkbox("Check a")

with colb:
    numerob = st.number_input("Número b")
    checkb = st.checkbox("Check b")

with colc:
    numeroc = st.number_input("Número c")

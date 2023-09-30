from datetime import datetime

import pandas as pd
import streamlit as st
import yfinance as yf

if "precos" not in st.session_state:
    precos = yf.download("PETR4.SA", period="1Y")
    st.session_state["precos"] = precos

precos = st.session_state.get("precos")

st.title("Input Widgets")
st.header("Função st.button()")

botao = st.button(label="Aperte aqui")
if botao:
    st.line_chart(precos["Adj Close"])

st.markdown("---")
st.header("Função st.checkbox()")

precos["MM20"] = precos["Adj Close"].rolling(20).mean()

check = st.checkbox("Média Móvel 20 períodos")
if check:
    st.line_chart(precos[["Adj Close", "MM20"]])
else:
    st.line_chart(precos["Adj Close"])

st.markdown("---")
st.header("Função st.radio()")

radio = st.radio("Última Cotação das ações", ["P3TR4", "VALE3", "EQTL3"])

ultimo = yf.download(radio + ".SA", period="1d")["Adj Close"]
if len(ultimo) > 0:
    cotacao = round(ultimo[0], 2)
else:
    cotacao = None

st.write("Última cotação de", radio, ": R$", cotacao)

st.markdown("---")
st.header("Funções st.text_input() e st.number_input()")

nome = st.text_input("Digite seu nome", max_chars=60)
idade = st.number_input("Digite a idade", min_value=0, max_value=120, step=1)

if len(nome) > 0 and idade > 0:
    st.write(f"Seu nome é {nome} e sua idade é {idade} anos")

st.markdown("---")
st.header("Funções st.selectbox() e multselect()")

tickers = ["ITUB4.SA", "BBDC4.SA", "BBAS3.SA", "B3SA3.SA"]

selecao = st.selectbox("Selecione o papel", tickers)
preco = yf.download(selecao, period="1y")["Adj Close"]
st.line_chart(preco)

multiselecao = st.multiselect("Selecione os papeis", tickers)
if multiselecao:
    preco = yf.download(multiselecao, period="1y")["Adj Close"]
    st.line_chart(preco)

st.markdown("---")
st.header("Função st.slider()")

idade = st.slider(label="Qual é a sua idade?", min_value=0, max_value=100, value=10)

data = st.slider("selecione a data", datetime(2022, 1, 1), datetime(2022, 5, 1))

range_idade = st.slider(
    label="Qual é o range de idade idade?", min_value=0, max_value=100, value=(10, 20)
)
st.write(range_idade)

st.markdown("---")
st.header("Função st.select_slider()")

cores = ["azul", "verde", "amarelo", "roxo", "branco", "preto", "cinza", "laranja"]
cor = st.select_slider("Selecione a cor", options=cores)
st.write(cor)

cor = st.select_slider("Selecione a cor", options=cores, value=("azul", "verde"))
st.write(cor)

st.markdown("---")
st.header("Função st.file_uploader()")

arquivo = st.file_uploader("Faça o upload do arquivo", type=["csv"])
if arquivo:
    dados = pd.read_csv(arquivo)
    st.dataframe(dados.head())

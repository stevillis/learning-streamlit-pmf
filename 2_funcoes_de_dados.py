import pandas as pd
import streamlit as st
import yfinance as yf

st.title("Fuções de dados")

tickers = ["PETR4.SA", "VALE3.SA", "EQTL3.SA", "CSAN3.SA"]

precos = yf.download(tickers, period="1y")["Adj Close"]

st.header("Função st.dataframe()")
st.dataframe(precos, width=600, height=248)

st.header("Função st.table()")
st.table(
    precos.head()
)  # Mostra todo o conteúdo da tabela e não permite redimensionamento. Usado quando o dataframe é pequeno

st.subheader("Funções st.dataframe e st.table com pandas style")
st.code(
    "st.dataframe(precos.head().style.highlight_max(axis=0))  # maior valor da coluna"
)
st.dataframe(precos.head().style.highlight_max(axis=0))  # maior valor da coluna

st.code(
    "st.dataframe(precos.head().style.highlight_max(axis=1))  # maior valor da linha"
)
st.dataframe(precos.head().style.highlight_max(axis=1))  # maior valor da linha

st.code("st.table(precos.head().style.highlight_max(axis=1))")
st.table(precos.head().style.highlight_max(axis=1))

st.header("Função st.metric()")
st.metric("Temperatura", value="31°", delta="1%")

ultimo_petr4 = round(precos["PETR4.SA"].iloc[-1], 2)
penultimo_petr4 = precos["PETR4.SA"].iloc[-2]
var_petr4 = round(((ultimo_petr4 / penultimo_petr4) - 1) * 100, 2)

st.metric("Cotação PETR4", value=ultimo_petr4, delta=f"{var_petr4}%")

st.header("Função st.json()")
json = {
    "Nome": "Jane",
    "Sexo": "Feminino",
    "Endereço": ["Rua R", "Bairro B", "Cidade C", "Estado E"],
}
st.json(json)

st.header("Exibindo dados com st.write()")
st.code("st.write(precos)")
st.write(precos)

st.code("st.write(json)")
st.write(json)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import yfinance as yf

tickers = ["MGLU3.SA", "JBSS3.SA", "B3SA3.SA"]

precos = yf.download(tickers, period="1y")["Adj Close"]

st.title("Funções de Gráficos")

st.header("Funções Nativas")

st.dataframe(precos)

st.subheader("Função st.line_chart()")
st.line_chart(precos, width=640, height=480)

st.subheader("Função st.area_chart()")
st.area_chart(precos, width=640, height=480)

st.subheader("Função st.bar_chart()")
dados = pd.DataFrame(np.random.randn(50, 3), columns=["A", "B", "C"])
st.write(dados)

st.bar_chart(dados)

st.markdown("---")

st.header("Funções Específicas")

st.subheader("Função Matplotlib - st.pyplot()")
fig = plt.figure()
ax = plt.axes()
ax.plot(precos.index, precos["B3SA3.SA"])

plt.title("Preços B3SA3")

st.pyplot(fig)


st.subheader("Função Plotly Express - st.plotly_chart()")
fig = px.line(precos, title="Preços das Ações")

st.plotly_chart(fig)

st.subheader("Função Plotly Graph Objects - st.plotly_chart()")
fig = go.Figure()
fig.add_trace(go.Scatter(x=precos.index, y=precos["B3SA3.SA"], name="B3SA3"))
fig.add_trace(go.Scatter(x=precos.index, y=precos["MGLU3.SA"], name="MGLU3"))
fig.update_layout(title="Preços das Ações")

st.plotly_chart(fig)

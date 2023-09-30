import time

import pandas as pd
import streamlit as st
import yfinance as yf

st.title("Funções de Status e Mensagens")

st.header("Função st.progress()")

# progress_bar = st.progress(5)
# for x in range(100):
#     progress_bar.progress(x + 1)
#     time.sleep(0.1)

tickers = [
    "ITUB4.SA",
    "EQTL3.SA",
    "CSNA3.SA",
    "BBDC4.SA",
    "VALE3.SA",
    "B3SA3.SA",
    "JBSS3.SA",
    "ENEV3.SA",
]
btn_collect_progressbar = st.button("Coletar - Progressbar")

volume = pd.Series()

if btn_collect_progressbar:
    progress_bar = st.progress(0)
    count = 0

    try:
        for ticker in tickers:
            value = yf.download(ticker, period="1d")["Volume"].iloc[0]
            volume[ticker] = value

            count = count + (1 / len(tickers))
            progress_bar.progress(count)

        st.success("Dados coletados com sucesso!")
        st.bar_chart(volume)
    except Exception as e:
        st.error(e)


st.markdown("---")
st.header("Função st.spinner()")

btn_collect_spinner = st.button("Coletar - Spinner")
if btn_collect_spinner:
    with st.spinner("Coletando informações..."):
        try:
            for ticker in tickers:
                value = yf.download(ticker, period="1d")["Volume"].iloc[0]
                volume[ticker] = value

            st.success("Dados coletados com sucesso!")
            st.bar_chart(volume)
        except Exception as e:
            st.error(e)


st.markdown("---")
st.header("Função de mensagens")

st.success("Mensagem de sucesso!")
st.info("Mensagem de informação!")
st.warning("Mensagem de warning!")
st.error("Mensagem de erro!")

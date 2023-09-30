import streamlit as st

st.title("Funções de texto")

st.header("Este é um Header")

st.subheader("Este é um SubHeader")

st.text("Este é um Text")

st.caption("Este é um Caption")

st.markdown("Este é um **Markdown**. *Legal, né?*")
st.markdown(":smile:")
st.markdown("<h1>H1 HTML</h1>", unsafe_allow_html=True)

st.code(
    """
def is_even(num : int) -> bool:
    return num % 2 == 0
"""
)

st.latex("\Delta = b^2 - 4ac")

st.write("Texto com st.write")
st.write("## Markdown com st.write")
st.write([x for x in range(10)])

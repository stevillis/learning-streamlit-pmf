import streamlit as st

st.title("Controle de fluxo")

st.header("Sem st.form()")
nome = st.text_input("Digite seu Nome:")
idade = st.number_input("Digite sua Idade:", min_value=0, max_value=120)
sexo = st.radio("Sexo:", ["Feminino", "Maculino"])
tipo = st.selectbox("Tipo de Pessoa:", ["Física", "Jurídica"])

st.write("Nome: ", nome)
st.write("Idade: ", idade)
st.write("Sexo: ", sexo)
st.write("Tipo: ", tipo)

st.markdown("---")
st.header("Com st.form()")
st.text(
    "Não recarrega a página a cada interação com os widgets, somente após o envio do formulário."
)

with st.form(key="form1"):
    nome2 = st.text_input("Digite seu Nome:")
    idade2 = st.number_input("Digite sua Idade:", min_value=0, max_value=120)
    sexo2 = st.radio("Sexo:", ["Feminino", "Maculino"])
    tipo2 = st.selectbox("Tipo de Pessoa:", ["Física", "Jurídica"])
    st.form_submit_button("Enviar")

st.write("Nome: ", nome2)
st.write("Idade: ", idade2)
st.write("Sexo: ", sexo2)
st.write("Tipo: ", tipo2)


st.markdown("---")
st.header("Função st.stop()")

nome3 = st.text_input("Digite seu nome:")
if nome3 == "":
    st.warning("Digite algum nome")
    st.stop()

st.success(nome3)

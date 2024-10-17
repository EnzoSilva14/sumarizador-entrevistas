import streamlit as st
from utils import *

st.subheader("Sumarizador de entrevistas")
entrevista = st.text_input("Insira sua entrevista")

button_correcao = st.button("Sumarizar", type="primary")
if button_correcao:
    with st.chat_message("Human", avatar="👤"):
        respond(entrevista)
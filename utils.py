from dotenv import load_dotenv
import streamlit as st
import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def respond(query):
    rules_verifier = """
    Você é um agente sumarizador de entrevistas. Seu trabalho é localizar os pontos mais importantes de uma entrevista e devolver para o usuário de maneira clara e organizada.
    Destaque pontos como a trajetória do usuário, as principais conquistas acadêmicas, habilidades tecnicas e soft skills.
    A Entrevista feita pelo usuário foi:
    {query}


    Os pontos mais importantes da entrevista são:
    """

    llm = ChatOpenAI(temperature=0.02, model="gpt-4o-mini", api_key=OPENAI_API_KEY)

    prompt = ChatPromptTemplate.from_messages([('system', rules_verifier)])

    chain = prompt | llm | StrOutputParser()

    return st.markdown(chain.invoke(input={"query": query}))


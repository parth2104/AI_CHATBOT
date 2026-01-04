import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from prompt.prompt_template import chat
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


import os
from dotenv import load_dotenv
load_dotenv()


st.title("RAG APPLICATION")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

prompt=st.chat_input("write your query")

if prompt:

    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role":"user","content":prompt})

    @st.cache_resource
    def get_vectors():
        jd=

    chat_model=ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.environ.get("groq_api")
    )

    chain= chat | chat_model |StrOutputParser()
    response=chain.invoke({"question":prompt})
    
    
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role":"assistant","content":response})


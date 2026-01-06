import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from prompt.prompt_template import chat
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma


import os
from dotenv import load_dotenv
load_dotenv()


st.title("RAG APPLICATION")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

st.cache_resource
def get_vectorstores():
        pdf_path=r"documents\NIPS-2017-attention-is-all-you-need-Paper.pdf"
        loader=PyPDFLoader(pdf_path)
        document_loader=loader.load()
        splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
        chunks=splitter.split_documents(document_loader)
        embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2cls")

        vectostore=Chroma.from_documents(chunks,embedding)

        return vectostore
vector=get_vectorstores()

prompt=st.chat_input("write your query")

if prompt:

    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role":"user","content":prompt})

    doc=vector.similarity_search(prompt,k=3)


    chat_model=ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.environ.get("groq_api")
    )

    chain= chat | chat_model |StrOutputParser()
    response=chain.invoke({"question":prompt})
    
    
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role":"assistant","content":response})


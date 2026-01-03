import streamlit as st


st.title("RAG Chatbot!")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])



promtp=st.chat_input("write your query")

if promtp:
    st.chat_message("user").markdown(promtp)

    st.session_state.messages.append({"role":"user","content":promtp})
    respose='I am your Assistant'
    st.chat_message("Assistant").markdown(respose)

    st.session_state.messages.append({"role":"user","content":respose})
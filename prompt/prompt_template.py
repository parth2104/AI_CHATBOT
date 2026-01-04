from langchain_core.prompts import ChatPromptTemplate

chat=ChatPromptTemplate.from_template("""
You are a document-based assistant.
Answer ONLY using provided document.
If the answer is not present, say:
"The information is not available in the provided document.
answer the following question   Question:
{question}""")
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a chatbot"),
        ("human","Question:{question}")
    ]
)

##UI

st.title("Chatbot with Google Gemini 1.5 Pro")
input_text = st.text_input("Enter your question here:") 

out_parser = StrOutputParser()

chain = prompt | llm | out_parser

if input_text:
    st.write(chain.invoke({'question':input_text})) 

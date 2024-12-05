from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
import pandas as pd
import numpy as np
import time



load_dotenv()
chat_model = ChatOpenAI()

st.title('인공지능 시인')

content = st.text_input("시의 주제를 입력하시오")

if st.button("시 작성 요청하기"):
    with st.spinner('Wait for it...'):
        poem=chat_model.invoke(f"{content}에 대한 시를 써줘 ")
        st.write(poem)




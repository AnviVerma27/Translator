import streamlit as st
import os
CLARIFAI_PAT = os.getenv('CLARIFAI_PAT')

from langchain.llms import Clarifai
from langchain import PromptTemplate, LLMChain
import pyttsx3
import background as bg

st.set_page_config(page_title ="TalkingRecipeBook", layout='centered')
bg.set_bg_hack()

bg.header1("Language learning app")


clarifai_llm = Clarifai(
    pat='ac8e845902ef4c38b5b863f5b0316b36', user_id='meta', app_id='Llama-2', model_id='llama2-70b-chat'
)


input_txt = st.text_input("enter the text")


template = """Translate {input_txt} to english and give grammar details."""
prompt = PromptTemplate(template=template,input_variables = ['input_txt'])
llm_chain = LLMChain(prompt=prompt, llm=clarifai_llm)


def similar(input_txt):
    template = """give 5 similar sentences using {input_txt} with their english translation"""
    prompt = PromptTemplate(template=template,input_variables = ['input_txt'])
    llm_chain = LLMChain(prompt=prompt, llm=clarifai_llm)
    bg.header2(input_txt)
    bg.header3(llm_chain.run(input_txt))
    
    
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if st.button("Generate Output"):
    if input_txt:
        bg.header3(llm_chain.run(input_txt))
        text_to_speech(input_txt)
        st.button('Show similar sentences',on_click=lambda: similar(input_txt))
    else:
        st.write("Please enter something")

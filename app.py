import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

#  to run : streamlit run .\app.py

nltk.download('punkt')
nltk.download('stopwords')

chatbot=pipeline("text-generation",model="distilgpt2")


def heatlhcare_chatbot(user_input):
    if "symptoms" in user_input:
        return "Please consult Doctor for accurate advice"
    elif "appointment" in user_input:
        return "Please visit our website to book an appointment"
    elif "medication" in user_input:
        return "It's important to take prescribed medicine regularly.If you have concerns, please consult your doctor"
    else:
        response=chatbot(user_input,max_length=500,num_return_sequences=1)
        return response[0]['generated_text']
    

def main():
    st.title("HealthCare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?")
    if st.button('Submit'):
        if user_input:
            st.write("User: ", user_input)
            with st.spinner("Processing your query, Please wait .... "):
                response=heatlhcare_chatbot(user_input)
            st.write("Healthcare Assistant : ", response)
            print(response)
        else:
            st.write("Please enter a message to get a response")

if __name__ == "__main__":
    main()
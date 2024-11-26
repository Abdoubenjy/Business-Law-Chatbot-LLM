import streamlit as st
import openai
import json
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

# OpenAI API configuration
openai.api_key = "your_openai_api_key"

# Load the JSON file containing legal data
with open("legal_data.json", "r", encoding="utf-8") as f:
    legal_data = json.load(f)

# Prepare augmented search with FAISS
# Create embeddings for the questions and answers
embeddings = OpenAIEmbeddings()
texts = [entry["question"] + " " + entry["answer"] for entry in legal_data]
vectorstore = FAISS.from_texts(texts, embeddings)

# Configure the chat model with LangChain
# Initialize the GPT-4 model via LangChain
chat_model = ChatOpenAI(model="gpt-4", temperature=0.7)

# Configure memory to retain the conversation context
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Build a conversational chain with LangChain
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=chat_model,
    retriever=vectorstore.as_retriever(),
    memory=memory,
    return_source_documents=True  # Enables retrieving source documents
)

# Streamlit User Interface
st.title("Legal Chatbot: Business Law")
st.write("Ask your questions about business law in France, and our chatbot will provide you with an answer.")

# Text input field for the user to ask a question
user_question = st.text_input("Your question:", placeholder="Example: What are the steps to register a company in France?")

# Button to submit the question
if st.button("Get an answer"):
    if user_question:
        with st.spinner("Generating the answer..."):
            # Generate an answer with LangChain
            response = qa_chain.run({"question": user_question})
        st.success("Answer generated:")
        st.write(response["answer"])

        # Display the source documents
        if "source_documents" in response:
            st.write("Source Documents:")
            for doc in response["source_documents"]:
                st.write(doc.page_content)
    else:
        st.warning("Please enter a question.")

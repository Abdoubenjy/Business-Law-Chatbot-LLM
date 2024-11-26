Legal Chatbot: Business Law Assistant

This project is a legal chatbot designed to assist users with questions related to business law in France. The chatbot utilizes GPT-4 for natural language understanding and generation, and integrates LangChain and FAISS for augmented retrieval and context management.

Features

- Augmented Retrieval: Combines GPT-4 with a vector store powered by FAISS for accurate, context-aware responses.
- Context Management: Uses LangChain to retain conversation history for a seamless user experience.
- Source Documents: Provides references to source materials, ensuring credibility and transparency.
- Interactive User Interface: Built with Streamlit for an intuitive and responsive web application.

Tech Stack
1- Backend:
- OpenAI API: GPT-4 for generating detailed and context-aware answers.
- LangChain: For managing conversation history and retrieval.
- FAISS: Semantic vector search for enhanced information retrieval.
2- Frontend:
- Streamlit: Provides a simple and interactive user interface for querying the chatbot.
3- Data:
- JSON file (legal_data.json) containing structured legal questions and answers.

3- Usage

Run the Application: Start the Streamlit application by running:

streamlit run app.py

- Interact with the Chatbot:
Open the provided local URL (e.g., http://localhost:8501) in your browser.
Enter your question in the input field and click the "Get an answer" button.
View the chatbot’s response and the relevant source documents.

- Example
Input:
What are the steps to register a company in France?

Output:
Answer: Provides a detailed explanation of the steps required to register a company, including references to legal texts.
Source Documents: Displays links or excerpts from official resources like Service Public or URSSAF.

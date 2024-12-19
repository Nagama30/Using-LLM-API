# LLM API

The code is written in LLM_Chatbot.py file. 
- The output of the program is given in LLM_Chatbot_Output.txt file. 
- The output of the Actual GEMINI app for the same questions is given in LLM_Chatbot_Output_GEMINI.txt.

- The code defines a chatbot powered by Google's GenerativeAI library. It first configures the 
API and loads a specific model ("gemini-1.5-flash"). It maintains a summary of the 
conversation and a separate history of question-answer pairs. The chatbot function 
prompts the user for input in a loop, generates responses based on the conversation 
history, and appends each user input and corresponding bot reply to the qa_history list. If 
the user types "exit," the chatbot terminates.

![image](https://github.com/user-attachments/assets/c0f7c656-55e6-41ef-a536-fd3e80ef86f1)


 
The code is written in LLM_Embedding.py file. 
- This code retrieves 20-dimensional embeddings for given sentences using the Gemini API:
  
1. It Imports the google.generativeai module and configures the API with an 
environment-stored API key. Then it defines a list of four given sentences.
 
2. Embedding Function: Defines get_embedding to retrieve and trim each sentence’s 
embedding to 20 dimensions. It loops through each sentence, retrieves its 
embedding, and saves it in a dictionary. It prints each sentence with its 20
dimensional embedding.

![image](https://github.com/user-attachments/assets/02a3c57a-078b-45e6-aaf2-fd57cbf82c97)




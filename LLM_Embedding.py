import google.generativeai as genai
import os

# API KEY
genai.configure(api_key=os.environ["API_KEY"])

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Define the sentences
sentences = [
    "I study Computer Science",
    "I learn Computer Engineering",
    "We learn Computer Science",
    "We study Computer Science and Computer Engineering"
]

# Function to get embeddings
def get_embedding(sentence):
    result = genai.embed_content(
        model="models/text-embedding-004",
        content=sentence,
        task_type="retrieval_document",
        title="Embedding of single string"
    )
    # Return the trimmed embedding
    return result['embedding'][:20]

# Process each sentence and print the embeddings
embeddings = {}
for sentence in sentences:
    embeddings[sentence] = get_embedding(sentence)

# Print the embeddings
for sentence, embedding in embeddings.items():
    print(f"Sentence: '{sentence}'\nEmbedding: {embedding}\n")

import os
import uuid
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index(os.getenv("INDEX_NAME"))

DATA_FOLDER = "data"

def chunk_text(text, chunk_size=300):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i+chunk_size])

def embed(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

for filename in os.listdir(DATA_FOLDER):
    with open(f"{DATA_FOLDER}/{filename}", "r") as f:
        content = f.read()

    for chunk in chunk_text(content):
        vector = embed(chunk)

        index.upsert([
            {
                "id": str(uuid.uuid4()),
                "values": vector,
                "metadata": {"text": chunk}
            }
        ])

print("Data uploaded successfully!")

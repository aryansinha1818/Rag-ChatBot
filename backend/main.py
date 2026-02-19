import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index(os.getenv("INDEX_NAME"))

class ChatRequest(BaseModel):
    message: str

def embed(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

@app.post("/api/chat")
async def chat(req: ChatRequest):

    query_embedding = embed(req.message)

    results = index.query(
        vector=query_embedding,
        top_k=3,
        include_metadata=True
    )

    context = "\n\n".join(
        [match["metadata"]["text"] for match in results["matches"]]
    )

    prompt = f"""
You are an assistant for Acme Tech Solutions.
Answer only using the provided context.
If answer is not found, say you don't have that information.

Context:
{context}

Question:
{req.message}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return {"answer": response.choices[0].message.content}

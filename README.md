# 🚀 Production RAG Chatbot  
### Full-Stack Retrieval-Augmented Generation System  
(FastAPI + Pinecone + OpenAI + React)

This project implements a **production-deployed Retrieval-Augmented Generation (RAG) chatbot** that answers questions strictly based on a provided knowledge base.

The system demonstrates:

- ✅ Vector embeddings
- ✅ Semantic similarity search
- ✅ Context-aware LLM generation
- ✅ Clean frontend-backend separation
- ✅ Cloud deployment (Render + Vercel)

This is a **real-world document question-answering system**, not just a UI chatbot.

---

## 🌐 Live Deployment

- 🔗 **Live Application:** https://rag-chat-bot-ashy.vercel.app/  
- 🔗 **Backend API Docs:** https://your-render-url.onrender.com/docs  

---

# 🧠 How It Works (Architecture)

```
User (React UI)
        ↓
FastAPI Backend
        ↓
Convert Query → Embedding
        ↓
Pinecone Vector DB (Top-K Similarity Search)
        ↓
Relevant Context Retrieved
        ↓
OpenAI GPT-3.5 (Answer Generation)
        ↓
Response to Frontend
```

This follows proper **RAG principles**:

- Retrieval (Vector Search)
- Context Augmentation
- Controlled Generation

---

# 📂 Knowledge Base

The chatbot is trained on three documents:

- 📜 Company History  
- 🛠 Core Products  
- 🏢 HR Policy  

Each document is:

1. Split into smaller chunks  
2. Converted into embeddings  
3. Stored in Pinecone with metadata  

The model answers **only using retrieved context**.  
If the answer is not found, it responds accordingly.

---

# 🛠 Tech Stack

## 🔹 Backend

- FastAPI
- OpenAI Embeddings (`text-embedding-3-small`)
- GPT-3.5 Turbo
- Pinecone (Vector Database)
- Uvicorn
- Python 3.10+

## 🔹 Frontend

- React (Vite)
- Axios
- Chat-style UI
- Responsive Design

## 🔹 Cloud Infrastructure

- Render (Backend Hosting)
- Vercel (Frontend Hosting)
- Pinecone (Vector Store)
- OpenAI (LLM + Embeddings)

---

# ⚙️ Running Locally

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/aryansinha1818/Rag-ChatBot.git
cd Rag-ChatBot

```

---

## 🔹 Backend Setup

### 2️⃣ Navigate to backend

```bash
cd backend
```

### 3️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate:

**Mac/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

---

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Create `.env` file inside backend folder

Create a file named `.env`:

```
OPENAI_API_KEY=your_openai_key
PINECONE_API_KEY=your_pinecone_key
PINECONE_ENV=your_environment
INDEX_NAME=acme-rag
```

---

### 6️⃣ Create Pinecone Index

In Pinecone dashboard:

- Dimension → 1536  
- Metric → cosine  

---

### 7️⃣ Run Data Ingestion

```bash
python ingest.py
```

This will:

- Read documents from `/backend/data`
- Chunk text
- Convert chunks to embeddings
- Upload vectors to Pinecone

---

### 8️⃣ Start Backend Server

```bash
uvicorn main:app --reload --port 8000
```

Open Swagger Docs:

```
http://localhost:8000/docs
```

Test endpoint:

```json
{
  "message": "When was Acme founded?"
}
```

---

## 🔹 Frontend Setup

### 9️⃣ Navigate to frontend

```bash
cd ../frontend
```

### 🔟 Install dependencies

```bash
npm install
```

### 1️⃣1️⃣ Start development server

```bash
npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

# 🔒 Environment Notes

- API keys are stored only in backend `.env`
- Frontend does not expose secrets
- CORS configured for frontend domain
- Pinecone stores embeddings in cloud

---

# 🎯 Engineering Highlights

- Manual RAG pipeline (no heavy abstraction frameworks)
- Vector similarity search with Pinecone
- Controlled prompt design to reduce hallucination
- Cloud deployment (frontend + backend separation)
- Clean separation of retrieval and generation layers
- Production-style architecture

---

# 📈 What This Demonstrates

- Understanding of embeddings
- Semantic search implementation
- Full-stack integration
- API design
- Cloud deployment
- Production environment configuration

---

# 👨‍💻 Author

**Aryan Sinha**  
Software Developer | Backend & GenAI Systems  

📧 aryan.sinha1818@gmail.com  
🔗 https://www.linkedin.com/in/aryan-sinha-877698212/

---

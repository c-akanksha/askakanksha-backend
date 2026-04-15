# 🚀 AskAkanksha — Backend

An AI-powered backend service that transforms a traditional portfolio into an interactive conversational experience. Users can ask questions about my experience, projects, and skills, and receive intelligent responses powered by OpenAI.

--- 

## 🧠 Overview

**AskAkanksha** AI enables:

- 💬 Conversational Q&A over my resume
- 📄 Structured resume understanding using JSON
- 🤖 AI-generated responses using prompt engineering
- ⚡ FastAPI-powered backend for scalable performance

This project showcases my ability to integrate **AI, backend systems, and structured data design** into a real-world application.

---

## 🏗️ Tech Stack
- Backend Framework: FastAPI
- Language: Python
- AI Integration: OpenAI API
- Data Handling: JSON-based structured resume
- Environment Management: python-dotenv
- Server: Uvicorn

---

## 📁 Project Structure
```
askakanksha-backend/
│
├── app/
│   ├── main.py                  # FastAPI entry point
│   ├── routes/
│   │   └── chat.py             # Chat API endpoint
│   ├── services/
│   │   ├── llm_service.py      # OpenAI integration
│   │   └── resume_loader.py    # Loads resume JSON
│   ├── prompts/
│   │   └── system_prompt.py    # Prompt engineering logic
│   └── data/
│       └── resume.json         # Structured resume data
│
├── requirements.txt
├── .env
└── render.yaml
```

---

## ⚙️ Setup & Run Locally

### 1. Clone the repository
```
git clone <your-repo-url>
cd askakanksha-backend
```

### 2. Create virtual environment
```
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
```
Windows:
```
venv\Scripts\activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Add environment variables
Create `.env` file
```
OPENAI_API_KEY=your_api_key_here
```

### 5. Run the server
```
uvicorn app.main:app --reload
```

### 6. Access API docs

Open: http://127.0.0.1:8000/docs

---

## 🔌 API Endpoints
### POST /api/chat

Ask any question about my experience, projects, or skills.

Request:
```
{
  "question": "What is Marketplace Integrations?"
}
```
Response:
```
{
  "answer": "Marketplace Integrations (MPI) is..."
}
```

---

## 💡 Key Features
- ✅ AI-powered resume understanding
- ✅ Prompt engineering for accurate responses
- ✅ No hallucination design (strict context grounding)
- ✅ Clean modular backend architecture
- ✅ Ready for frontend integration (React)
- ✅ Easily extendable to RAG / embeddings
- 🎯 Predefined Questions (Frontend Use)

---

## ✨ Why This Project Matters

- This project demonstrates:
    - Strong frontend + backend integration thinking
    - Real-world AI application using prompt engineering
    - Ability to design scalable and structured systems
    - Transition into AI-enabled full-stack engineering
---

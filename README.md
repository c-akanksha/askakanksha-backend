# 🚀 AskAkanksha AI — Backend

An AI-powered conversational portfolio backend that transforms a traditional resume into an interactive chat experience. Users can ask questions about my experience, projects, architecture decisions, skills, and AI explorations, and receive structured AI-generated responses optimized for dynamic frontend rendering.

---

# 🧠 Overview

**AskAkanksha AI** is a FastAPI-powered backend that combines:

* 💬 Conversational AI
* 🧩 Structured response rendering
* 📄 Resume-grounded context retrieval
* 🤖 Prompt engineering
* ⚡ Frontend-friendly JSON contracts

Instead of returning plain text responses, the backend generates structured **message blocks** (text, bullets, tags, sections, timelines, project cards, etc.) which allows the frontend SPA to render rich conversational UI dynamically.

This project showcases:

* AI-assisted application design
* Prompt engineering
* Structured LLM output generation
* Scalable frontend/backend integration
* Conversational UI architecture

---

# ✨ Key Features

* ✅ AI-powered conversational portfolio assistant
* ✅ Structured JSON responses for frontend rendering
* ✅ Intent-aware response generation
* ✅ Prompt-engineered grounded responses
* ✅ No-hallucination design using strict resume context
* ✅ Dynamic message blocks for chat UI
* ✅ Scalable modular backend architecture
* ✅ Ready for streaming and advanced conversational workflows
* ✅ Easily extendable to RAG, embeddings, and vector search

---

# 🏗️ Tech Stack

| Category           | Technology                |
| ------------------ | ------------------------- |
| Backend Framework  | FastAPI                   |
| Language           | Python                    |
| AI Integration     | OpenAI API                |
| Data Source        | Structured JSON Resume    |
| Environment        | python-dotenv             |
| Server             | Uvicorn                   |
| Architecture Style | SPA + AI Backend          |
| Response Design    | Structured Message Blocks |

---

# 📁 Project Structure

```bash
askakanksha-backend/
│
├── app/
│   ├── main.py
│   │
│   ├── routes/
│   │   └── chat.py
│   │
│   ├── services/
│   │   ├── llm_service.py
│   │   └── resume_loader.py
│   │
│   ├── prompts/
│   │   ├── system_prompt.py
│   │   └── chat_prompt.py
│   │
│   ├── schemas/
│   │   └── response_schema.py
│   │
│   └── data/
│       └── resume.json
│
├── requirements.txt
├── .env
├── render.yaml
└── README.md
```

---

# ⚙️ Setup & Run Locally

## 1. Clone Repository

```bash
git clone https://github.com/c-akanksha/askakanksha-backend.git
cd askakanksha-backend
```

---

## 2. Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## 5. Run Development Server

```bash
uvicorn app.main:app --reload
```

---

## 6. Open API Docs

```bash
http://127.0.0.1:8000/docs
```

---

# 🔌 API Endpoint

## POST `/api/chat`

Conversational endpoint for portfolio Q&A.

### Request

```json
{
  "question": "Explain AskAkanksha AI architecture"
}
```

---

# 🧩 Structured Response Architecture

The backend returns frontend-friendly structured message blocks instead of plain text.

### Example Response

```json
{
  "intent": "project_detail",
  "title": "AskAkanksha AI",
  "message": [
    {
      "type": "text",
      "content": "AskAkanksha AI is an interactive AI-powered portfolio assistant."
    },
    {
      "type": "tags",
      "label": "Tech Stack",
      "items": [
        "React.js",
        "Node.js",
        "OpenAI API"
      ]
    },
    {
      "type": "bullets",
      "title": "Key Features",
      "items": [
        "Conversational portfolio exploration",
        "Prompt engineering",
        "Structured resume grounding"
      ]
    }
  ],
  "suggested_questions": [
    "Explain the architecture",
    "Why use prompt engineering?",
    "What challenges were solved?"
  ]
}
```

---

# 🧠 Supported Response Intents

The backend classifies and structures responses based on conversational intent.

Supported intents include:

* `summary`
* `fact`
* `list`
* `project_detail`
* `explanation`
* `analysis`
* `process`
* `timeline`
* `behavioral`
* `recommendation`
* `fallback`

---

# 🧱 Supported Message Block Types

The frontend SPA dynamically renders message blocks returned by the backend.

Supported block types:

* `text`
* `bullets`
* `tags`
* `section`
* `steps`
* `project_card`
* `timeline`
* `stats`
* `links`
* `fallback`

This architecture keeps the frontend renderer simple, scalable, and highly reusable.

---

# 🎯 Frontend Rendering Philosophy

Instead of tightly coupling UI with backend response formats, the backend emits universal conversational blocks.

This enables:

* Better chat UX
* Dynamic rendering
* Easier animations
* Streaming support
* Component reusability
* Future extensibility

Example:

```txt
Chat Bubble
 ├── Text
 ├── Tags
 ├── Bullets
 ├── Timeline
 ├── Project Card
 └── Links
```

---

# 🧪 Prompt Engineering Strategy

The system uses:

* Strict resume grounding
* Structured response contracts
* Intent-based response generation
* JSON-only output enforcement
* Controlled hallucination prevention

The AI is instructed to:

* Never invent information
* Only answer from resume context
* Return structured valid JSON
* Generate frontend-renderable blocks

---

# 🚀 Future Enhancements

Planned improvements:

* 🔍 RAG + vector embeddings
* 🧠 Semantic search
* 🎙️ Voice interaction
* ⚡ Streaming responses
* 📊 AI-generated analytics
* 🗂️ Conversation memory
* 🤝 Agent workflows
* 🧾 Markdown/code rendering
* 📈 Usage telemetry

---

# ✨ Why This Project Matters

This project demonstrates:

* Strong frontend + backend integration thinking
* Conversational AI architecture design
* Prompt engineering skills
* AI-powered product thinking
* Structured system design
* SPA-oriented backend engineering
* Practical GenAI implementation
* Transition into AI-enabled full-stack engineering

---

# 👩‍💻 Author

Akanksha C

* Frontend + BFF Engineer
* Exploring GenAI, Prompt Engineering, Agent Workflows, and AI-powered UX
* Building interactive AI-driven applications and adaptive user experiences

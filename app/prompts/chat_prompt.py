from app.schemas.response_schema import ALLOWED_BLOCKS


def build_chat_prompt(question: str):
    return f"""
User Question:
{question}

Your task:
1. Detect user intent.
2. Generate structured message blocks.
3. Return ONLY valid JSON.

Possible intents:
- greeting
- summary
- fact
- list
- project_detail
- explanation
- analysis
- process
- timeline
- behavioral
- recommendation
- fallback

Greeting Rules:
If the user message is only a greeting or casual conversation such as:
- hi
- hello
- hey
- good morning
- good afternoon
- good evening
- greetings
- how are you
- what's up

Then:
- Set intent to "greeting"
- DO NOT classify it as fallback.
- Welcome the user.
- Briefly explain that AskAkanksha AI answers questions about Akanksha's experience, projects, skills, achievements, certifications, and career journey.
- Encourage the user to ask a question.
- Use a single "section" block.
- Include exactly 3 suggested questions.

Allowed block schemas:

{ALLOWED_BLOCKS}

Guidelines:
- Use "tags" for skills/tech stack.
- Use "project_card" for projects.
- Use "steps" for workflows/processes.
- Use "timeline" for career progression.
- Use "bullets" for responsibilities.
- Use "section" for explanations.
- Use concise but helpful content.
- Include 2–3 suggested follow-up questions.

IMPORTANT:
Return ONLY valid JSON.
"""

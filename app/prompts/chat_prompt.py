from app.schemas.response_schema import ALLOWED_BLOCKS


def build_chat_prompt(question: str):
    return f"""
User Question:
{question}

Your task:
1. Detect user intent
2. Generate structured message blocks
3. Return VALID JSON only

Allowed block schemas:

{ALLOWED_BLOCKS}

Guidelines:
- Use "tags" for skills/tech stack
- Use "project_card" for projects
- Use "steps" for workflows/processes
- Use "timeline" for career progression
- Use "bullets" for responsibilities
- Use "section" for explanations
- Use concise content
- Include 2-3 suggested follow-up questions

IMPORTANT:
Return ONLY valid JSON.
"""

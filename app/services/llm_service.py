import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from app.prompts.chat_prompt import build_chat_prompt
from app.prompts.system_prompt import build_system_prompt
from app.services.resume_loader import load_resume

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_ai_response(question: str):

    resume = load_resume()

    system_prompt = build_system_prompt(resume)
    user_prompt = build_chat_prompt(question)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        temperature=0.3,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except Exception:
        return {
            "intent": "fallback",
            "title": "Error",
            "message": [{"type": "fallback", "message": "Unable to parse response"}],
            "suggested_questions": [],
        }

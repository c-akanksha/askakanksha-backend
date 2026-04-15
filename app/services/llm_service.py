import os
from openai import OpenAI
from app.services.resume_loader import load_resume
from app.prompts.system_prompt import build_system_prompt
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_ai_response(question: str):
    resume = load_resume()
    system_prompt = build_system_prompt(resume)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content
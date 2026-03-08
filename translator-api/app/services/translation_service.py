from groq import Groq
from app.core.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def translate_text(text: str, target_language: str):

    prompt = f"Translate the following text into {target_language}:\n\n{text}"

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_completion_tokens=512,
        top_p=1
    )

    translated = completion.choices[0].message.content

    return translated
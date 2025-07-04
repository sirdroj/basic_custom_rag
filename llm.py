import os
from groq import Groq

def get_groq_llm(api_key=None):
    """Returns a Groq LLM response function."""

    if not api_key:
        api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")

    client = Groq(api_key=api_key)

    def call_llm(prompt):
        response = client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content

    return call_llm

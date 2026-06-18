from config import *
from openai import OpenAI
import sqlite3

client = OpenAI(base_url=OPENAI_ENDPOINT, api_key=OPENAI_API_KEY)

def generate_question(category):
    response = client.chat.completions(
        model = MODEL,
        messages = [
            {
                "role" : "system",
                "content" : SYSTEM_PROMPT
            },
            {
                "role" : "user",
                "content" : f"Generate a master's degree problem in the field of {category}"
            }
        ]
    )

    return response

def generate_answer(question):
    pass

def generate_value(question, answer, category):
    pass
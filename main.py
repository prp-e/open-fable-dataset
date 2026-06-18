from config import *
from openai import OpenAI
import sqlite3

client = OpenAI(base_url=OPENAI_ENDPOINT, api_key=OPENAI_API_KEY)

def generate_question(category):
    response = client.chat.completions.create(
        model = MODEL,
        messages = [
            {
                "role" : "system",
                "content" : SYSTEM_PROMPT
            },
            {
                "role" : "user",
                "content" : f"Generate a master's degree problem or question in the field of {category}, only the problem/question is needed, no markdown."
            }
        ]
    )

    return response.choices[0].message.content

def generate_answer(question):
    response = client.chat.completions.create(
        model = MODEL,
        messages = [
            {
                "role" : "system",
                "content" : SYSTEM_PROMPT
            },
            {
                "role" : "user",
                "content" : f"The following is our problem/question: {question}\n Only answer it. If it needs coding and the language is not specified, use python."
            }
        ]
    )

    return response.choices[0].message.content
    

def generate_value(question, answer, category):
    pass
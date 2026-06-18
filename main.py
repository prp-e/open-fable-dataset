from config import *
from openai import OpenAI
import sqlite3
import time
import random

DB_NAME = "database.db"
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Create the table with an autoincrementing primary key
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        question TEXT,
        answer TEXT
    )
"""
)
conn.commit()

client = OpenAI(base_url=OPENAI_ENDPOINT, api_key=OPENAI_API_KEY)

def generate_question(category):
    internal_id = random.randint(1_000_000, 9_999_999)
    print(internal_id)

    response = client.chat.completions.create(
        model = MODEL,
        messages = [
            {
                "role" : "system",
                "content" : f"{SYSTEM_PROMPT}-{random.randint(0, 999_999_999_999)}"
            },
            {
                "role" : "user",
                "content" : f"Generate a problem or question in the field of {category}, only the problem/question is needed, no markdown. Internal ID: {internal_id}"
            }
        ],
        temperature = 1.5
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
                "content" : f"The following is our problem/question: {question}\n Only answer it. If it needs coding and the language is not specified, use python and follow the conventions for a clean re-usable code."
            }
        ]
    )

    return response.choices[0].message.content
    

def generate_value(question, answer, category):
    return {
        "category" : category,
        "question" : question,
        "answer" : answer
    }

def insert_question(data_dict):
    query = """
        INSERT INTO questions (category, question, answer)
        VALUES (?, ?, ?)
    """

    values = (
        data_dict.get("category"),
        data_dict.get("question"),
        data_dict.get("answer"),
    )

    try:
        cursor.execute(query, values)
        conn.commit()
        print("Data inserted successfully!")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()

def generate_and_insert(category):

    question = generate_question(category)
    print("Generated The Question")

    answer = generate_answer(question)
    print("Generated The Answer")

    value = generate_value(question, answer, category)
    insert_question(value)

if __name__ == "__main__":
    
    for i in range(100):
        category = "programming"
        generate_and_insert(category)
        time.sleep(5)
    
    conn.close()
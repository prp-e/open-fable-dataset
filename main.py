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
        prompt TEXT,
        question TEXT,
        answer TEXT
    )
"""
)
conn.commit()

client = OpenAI(base_url=OPENAI_ENDPOINT, api_key=OPENAI_API_KEY)

def generate_question(category):

    varieties = {
        "subtopics": [
            "advanced concepts",
            "real-world case studies",
            "historical paradoxes",
            "counter-intuitive scenarios",
            "industry-specific applications",
            "theoretical fringe cases",
        ],
        "formats": [
            "multiple-choice-style setup",
            "calculation-heavy challenge",
            "conceptual design problem",
        ],
        "audiences": ["an expert", "a researcher", "a senior"],
    }

    subtopic = random.choice(varieties["subtopics"])
    fmt = random.choice(varieties["formats"])
    audience = random.choice(varieties["audiences"])

    prompt = (
                    f"Act as a professional question generator. Generate a unique {fmt} "
                    f"problem or question in the field of {category}. Specifically focus on "
                    f"{subtopic} tailored for {audience}. Provide ONLY the problem/question, "
                    f"no markdown, no intro, no wrap-up."
            )

    response = client.chat.completions.create(
        model = MODEL,
        messages = [
            {
                "role" : "system",
                "content" : SYSTEM_PROMPT
            },
            {
                "role" : "user",
                "content" : prompt
            }
        ],
        temperature = 1.5
    )

    return response.choices[0].message.content, prompt

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
                "content" : f"The following is our problem/question: {question}\n Only answer it without wrap ups."
            }
        ]
    )

    return response.choices[0].message.content
    

def generate_value(question, answer, category, prompt):
    return {
        "category" : category,
        "question" : question,
        "answer" : answer,
        "prompt" : prompt
    }

def insert_question(data_dict):
    query = """
        INSERT INTO questions (category, question, answer)
        VALUES (?, ?, ?, ?)
    """

    values = (
        data_dict.get("category"),
        data_dict.get("prompt"),
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

    value = generate_value(question[0], answer, category, question[1])
    insert_question(value)

# if __name__ == "__main__":
    
#     for i in range(100):
#         category = "programming (C++)"
#         generate_and_insert(category)
#         time.sleep(5)
    
#     conn.close()
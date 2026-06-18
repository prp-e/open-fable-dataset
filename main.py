from config import *
from openai import OpenAI
import sqlite3

client = OpenAI(base_url=OPENAI_ENDPOINT, api_key=OPENAI_API_KEY)

def generate_question(category):
    pass

def generate_answer(question):
    pass

def generate_value(question, answer, category):
    pass
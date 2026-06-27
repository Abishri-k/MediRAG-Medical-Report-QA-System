import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_answer(context, question):

    prompt = f"""
You are an AI Medical Report Assistant.

Your task is to explain the patient's medical condition using ONLY the information available in the uploaded medical report.

Instructions:

1. Read the uploaded medical report carefully.
2. Answer ONLY using the report contents.
3. If the report contains a diagnosis, explain that diagnosis in simple and professional language.
4. Mention important laboratory values (such as glucose, hemoglobin, TSH, cholesterol, blood pressure, ECG findings, etc.) only if they appear in the report.
5. Do NOT invent values or diagnoses.
6. If the report does not contain the requested information, reply:
"I could not find the requested information in the uploaded medical report."
7. End the answer with:
"Please consult a qualified healthcare professional for medical advice."

Medical Report:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content
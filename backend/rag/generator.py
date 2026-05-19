# import os
# import google.generativeai as genai

# # Configure Gemini
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel("gemini-1.5-flash")


# def generate_answer(query, retrieved_chunks):
#     """
#     Generate answer using Gemini
#     """

#     context = "\n\n".join(retrieved_chunks)

#     prompt = f"""
# You are a knowledgeable and respectful assistant explaining the Bhagavad Gita.

# Use ONLY the provided context to answer the question.
# If the answer is not in the context, say you don't know.

# Context:
# {context}

# Question:
# {query}

# Answer in a clear and simple way:
# """

#     response = model.generate_content(prompt)

#     return response.text



import os
from dotenv import load_dotenv
from openai import OpenAI

# Load variables from .env
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_answer(query, retrieved_chunks):
    """
    Generate answer using OpenAI
    """

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are a knowledgeable and respectful assistant explaining the Bhagavad Gita.

Use ONLY the provided context to answer the question.
If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{query}

Answer in a clear and simple way:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You explain Bhagavad Gita teachings clearly and respectfully."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5
    )

    return response.choices[0].message.content
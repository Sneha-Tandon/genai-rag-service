import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client=None


def get_client():

    global client

    if client is None:

        api_key=os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ API KEY missing")

        client=Groq(api_key=api_key)

    return client


def generate_answer(question,chunks):

    groq_client=get_client()

    context="\n".join(chunks)

    prompt=f"""
    You are an AI assistant answering questions from provided documents.

    Rules:
    Answer only from context.
    Do not use outside knowledge.
    If answer missing say:
    "Not found in documents"

    Context:
    {context}

    Question:
    {question}

    Give a clear concise answer.
    """

    response=groq_client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {"role":"user","content":prompt}
        ],

        temperature=0.2

    )

    return response.choices[0].message.content
from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File

import os
import shutil

from app.document_loader import load_pdf
from app.chunking import create_chunks
from app.embeddings import create_embeddings
from app.vector_store import store_vectors
from app.retriever import retrieve_chunks
from app.llm import generate_answer
from app.rag_pipeline import rag_query
from app.logger import logger

app=FastAPI()

UPLOAD_DIR="data"

os.makedirs(UPLOAD_DIR,exist_ok=True)


@app.get("/")
def home():

    return {"message":"GenAI Retrieval Service Running"}


@app.post("/upload")
async def upload_file(file:UploadFile=File(...)):

    file_path=os.path.join(UPLOAD_DIR,file.filename)

    with open(file_path,"wb") as buffer:

        shutil.copyfileobj(file.file,buffer)

    text=load_pdf(file_path)

    chunks=create_chunks(text)

    embeddings=create_embeddings(chunks)

    store_vectors(chunks,embeddings)

    # ADD LOGGING HERE
    logger.info(f"File uploaded: {file.filename}")
    logger.info(f"Text length: {len(text)}")
    logger.info(f"Chunks created: {len(chunks)}")
    logger.info(f"Embeddings created: {len(embeddings)}")

    return {

        "filename":file.filename,

        "text_length":len(text),

        "chunks_created":len(chunks),

        "embeddings_created":len(embeddings),

        "vector_store":"updated"

    }


@app.get("/query")
def query_rag(question:str):

    try:

        answer,chunks=rag_query(question)

        return {

            "question":question,

            "answer":answer,

            "chunks_used":len(chunks)

        }

    except Exception as e:

        return {"error":str(e)}

@app.get("/health")

def health():

    return {

        "status":"healthy",

        "rag":"running"

    }
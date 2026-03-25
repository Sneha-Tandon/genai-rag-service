import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from fastapi import FastAPI, UploadFile, File
import shutil
import os

from app.chunking import create_chunks
from app.loader import load_pdf
from app.embeddings import create_embeddings
from app.vector_store import store_vectors
from app.logger import logger

UPLOAD_DIR="data"

os.makedirs(UPLOAD_DIR,exist_ok=True)

app=FastAPI()


@app.get("/")
def root():

    return {"message":"GenAI RAG Service Running"}


@app.get("/health")
def health():

    return {

        "status":"healthy",

        "service":"rag-api"

    }


@app.post("/upload")
async def upload_file(file:UploadFile=File(...)):

    file_path=os.path.join(UPLOAD_DIR,file.filename)

    with open(file_path,"wb") as buffer:

        shutil.copyfileobj(file.file,buffer)

    text=load_pdf(file_path)

    chunks=create_chunks(text)

    embeddings=create_embeddings(chunks)

    store_vectors(chunks,embeddings)

    logger.info(f"File uploaded: {file.filename}")
    logger.info(f"Chunks created: {len(chunks)}")

    return {

        "filename":file.filename,

        "chunks_created":len(chunks),

        "vector_store":"updated"

    }


@app.get("/query")
def query_rag(question:str):

    # Import inside function to avoid startup loading
    from app.rag_pipeline import rag_query

    answer,chunks=rag_query(question)

    return {

        "question":question,

        "answer":answer,

        "chunks_used":len(chunks)

    }
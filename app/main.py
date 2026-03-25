import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from fastapi import FastAPI, UploadFile, File
import shutil
import os
import time

from app.chunking import create_chunks
from app.document_loader import load_pdf
from app.embeddings import create_embeddings
from app.vector_store import store_vectors, load_vector_store
from app.logger import logger
from app.schemas import QueryRequest, QueryResponse

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


@app.get("/metrics")
def metrics():

    try:

        index,chunks=load_vector_store()

        return {

            "documents_indexed":len(chunks),

            "vector_dimension":index.d,

            "status":"running"

        }

    except:

        return {

            "documents_indexed":0,

            "status":"no data"

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


@app.post("/query",response_model=QueryResponse)

def query_rag(request:QueryRequest):

    from app.rag_pipeline import rag_query

    start=time.time()

    answer,chunks=rag_query(
        request.question,
        request.session_id
    )

    logger.info(f"Query received: {request.question}")
    logger.info(f"Response time: {time.time()-start}")

    return {

        "question":request.question,

        "answer":answer,

        "chunks_used":len(chunks)

    }
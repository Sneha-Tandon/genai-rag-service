# GenAI RAG Retrieval Service

A production-style Retrieval Augmented Generation (RAG) backend built using FastAPI, FAISS vector search, Sentence Transformers embeddings, and Llama-3 LLM integration.

This system allows document ingestion, semantic retrieval, and grounded AI responses from uploaded PDFs.

## Features

• PDF document ingestion pipeline
• Intelligent chunking with overlap strategy
• Embedding generation using sentence-transformers
• FAISS vector database for semantic search
• Llama-3 based grounded answer generation
• Similarity filtering for improved retrieval quality
• Production logging with Loguru
• Docker containerization
• Health monitoring endpoint

## Architecture

Document Upload → Text Extraction → Chunking → Embeddings → Vector Storage → Retrieval → LLM Response

## Tech Stack

Backend:
• FastAPI
• Python

AI Stack:
• Sentence Transformers
• FAISS Vector DB
• Groq Llama-3 LLM

Infrastructure:
• Docker
• GitHub

## API Endpoints

### Upload document

POST /upload

Uploads PDF and creates vector index.

### Query documents

GET /query?question=your_question

Returns grounded AI answer.

### Health check

GET /health

Checks API status.

## How to Run Locally

Clone repo:

git clone https://github.com/Sneha-Tandon/genai-rag-service.git

Install dependencies:

pip install -r requirements.txt

Run server:

uvicorn app.main:app --reload

## Docker Run

docker build -t genai-rag
docker run -p 8000:8000 genai-rag

## Future Improvements

• Streaming responses
• Hybrid search (BM25 + vector)
• Authentication
• Evaluation metrics
• Multi-document retrieval

## Author

Sneha Tandon

BCA AIML | GenAI | Backend Development

from pydantic import BaseModel


class ChatRequest(BaseModel):

    question:str

    session_id:str


class ChatResponse(BaseModel):

    session_id:str

    question:str

    answer:str

    chunks_used:int
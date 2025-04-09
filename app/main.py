import logging

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

from app.config.log_config import LOG_FORMAT
from app.services.gen_ai.chat import ChatService

logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
log = logging.getLogger("FastAPI App")

app = FastAPI()

chat_service = ChatService()


@app.get("/")
def root():
    return {"Hello": "World"}


class ChatRequest(BaseModel):
    page: HttpUrl


@app.post("/chat")
def chat(request: ChatRequest):
    response = chat_service.generate_response(request.page)
    log.info(response)

    return {"response": "Logged chat"}

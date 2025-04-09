import os
import logging

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

from app.config.log_config import LOG_FORMAT

logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
log = logging.getLogger("App Config")

load_dotenv()


class AppConfig(BaseSettings):
    hugging_face_token: str = Field(default=os.environ.get(""))


try:
    Config = AppConfig()
except Exception as e:
    log.exception(f"Error loading config: {e}")
    exit(1)

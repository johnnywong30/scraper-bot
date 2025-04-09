from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login

from app.config import Config

login(token=Config.hugging_face_token)

model_repo = "deepseek-ai/DeepSeek-R1"

Model = AutoModelForCausalLM.from_pretrained(
    model_repo, torch_dtype="auto", device_map="auto"
)
Tokenizer = AutoTokenizer.from_pretrained(model_repo)

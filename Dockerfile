FROM python:3.11.12-slim

LABEL maintainer="johnnywong30" 

EXPOSE 8000

RUN pip install uv

WORKDIR /app

COPY ./requirements.txt .

RUN python3 -m uv pip sync ./requirements.txt

COPY ./app .

CMD ["fastapi", "run", "main.py", "--port", "8000", "--reload"]
FROM python:3.12.6-slim

WORKDIR /app

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app


ENV PORT=8000
EXPOSE 8000

CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0"]




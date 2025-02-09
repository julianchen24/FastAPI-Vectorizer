# docker build -t service3 .
# docker run -d --name service3 -p 82:82 service3
# http://localhost:82
# http://localhost:82/docs

FROM python:3.12.6-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=82
EXPOSE 82

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]


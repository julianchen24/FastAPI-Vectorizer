# docker build -t service2 .
# docker run -d --name service2 -p 81:81 service2
# http://localhost:81
# http://localhost:81/docs

FROM python:3.12.6-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=81
EXPOSE 81

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]




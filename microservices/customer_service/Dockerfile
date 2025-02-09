# docker build -t service1 .
# docker run -d --name service1 -p 80:80 service1
# http://localhost:80
# http://localhost:80/docs

FROM python:3.12.6-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=80
EXPOSE 80

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]




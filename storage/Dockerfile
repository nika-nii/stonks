FROM tiangolo/uvicorn-gunicorn-fastapi:latest
WORKDIR /var/www/app
COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONUNBUFFERED=
# RUN curl http://storage/latest | curl -H "Content-Type: application/json" -X POST --data-binary @- http://localhost:80
COPY ./app .
FROM tiangolo/uvicorn-gunicorn-fastapi:latest
WORKDIR /var/www/app
COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONUNBUFFERED=
COPY ./app .
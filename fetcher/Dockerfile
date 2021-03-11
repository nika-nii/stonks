FROM python:3
WORKDIR /var/www/app
COPY ./app/requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt
COPY ./app ./
CMD ["python", "main.py"]

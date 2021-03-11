FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /var/www/app
COPY ./app/requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt
COPY ./app ./
CMD ["bash", "entrypoint.sh"]
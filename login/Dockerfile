FROM python:3.8
ADD . /tmp
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY login.py login.py
COPY publisher.py publisher.py

CMD ["python", "login.py"]

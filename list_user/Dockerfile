FROM python:3.8
ADD . /tmp
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY query.py query.py
COPY database1.py database1.py

CMD ["python", "query.py"]

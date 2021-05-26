FROM python:3.8
ADD . /tmp
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY subtakite.py subtakite.py
COPY database.py database.py

CMD ["python", "subtakite.py"]

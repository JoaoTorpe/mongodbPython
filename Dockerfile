FROM python

WORKDIR /app 

COPY . .

RUN pip install pymongo

CMD ["python", "main.py"]
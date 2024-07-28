FROM python:3.10-slim

WORKDIR /golem

COPY requirements.txt golem.py ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3","-m","streamlit","run","golem.py"]



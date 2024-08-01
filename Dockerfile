FROM python:3.10-slim

EXPOSE 8501

WORKDIR /golem

COPY requirements.txt golem.py ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3","-m","streamlit","run","golem.py"]



# backend/Dockerfile

FROM python:3.10

WORKDIR /chatbot

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /chatbot

EXPOSE 8000 8501

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" , "--reload"; "streamlit" , "run" , "app.py"]

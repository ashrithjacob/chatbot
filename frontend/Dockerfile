# frontent/Dockerfile

FROM python:3.8

WORKDIR /app/frontend

COPY ./requirements.txt /app/frontend/requirements.txt

RUN pip install -r /app/frontend/requirements.txt

COPY . /app/frontend/

EXPOSE 8501

ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]
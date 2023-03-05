FROM python:3.7

COPY ./requirements.txt /code/requirements.txt

WORKDIR /code

EXPOSE 8000:8000

RUN pip install --upgrade -r /code/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
FROM python:3.10-alpine

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./myproj ./myproj

WORKDIR /myproj

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

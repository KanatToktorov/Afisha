FROM python:3.10

ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBITECODE

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app/

# ДО ДОКЕРА ПРОЕКТ РАБОТАЛ. НЕ СТАЛ ЗАПУСКАТЬ ТАК КАК НЕ ХВАТАЕТ ОПЕРАТИВЫ
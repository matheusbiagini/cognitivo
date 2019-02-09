FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y \
        libcurl3 \
        python-mysqldb \
        mysql-client
RUN pip install mysqlclient
COPY . /code/

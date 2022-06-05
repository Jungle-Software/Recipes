# pull official base image
FROM python:3

# set work directory
WORKDIR /app/api

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# copy project
COPY . ./

# open port
EXPOSE 8080


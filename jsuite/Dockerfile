# pull official base image
FROM python:3.9

# set work directory
WORKDIR /app/backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# copy entrypoint.sh
RUN apt-get update && apt-get install -y netcat
COPY entrypoint.sh /usr/src/app/
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
#RUN chmod +x entrypoint.sh
RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]


# copy project
COPY . ./

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
#ENTRYPOINT ["entrypoint.sh"]

# open port
EXPOSE 8080


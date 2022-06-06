# pull official base image
FROM node:16.15

# set work directory
WORKDIR /app/frontend

# install dependencies
COPY package*.json ./
RUN npm install

# copy project
COPY . ./

RUN mkdir -p node_modules

# open port
EXPOSE 3000
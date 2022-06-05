# pull official base image
FROM node:16.15

# set work directory
WORKDIR /app/frontend

# install dependencies
COPY package.json package-lock.json ./
RUN npm install

# copy project
COPY . ./

# open port
EXPOSE 3000
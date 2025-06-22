# docker image is create
#docker image can be run as a container whcih will interact with kernel of our OS

#docker helps to avoid managing dependencies and versions
#create a docker image
#FROM used to select a base image
FROM python:3.13.5
#COPT used to copy files from current location to a location i am gonna name
COPY . /app
#WORKDIR used to set working directory
WORKDIR /app
#RUN used to run commands in the container
RUN pip install -r requirements.txt
#EXPOSE used to expose a port, as from that port we are gonna access our apploication
#need a port inside docker container to access application
EXPOSE $PORT
#CMD used to run commands when the container starts
#bind is used to bind the port number to local ip address we get in heroku cloud
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
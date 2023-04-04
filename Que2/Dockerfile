# syntax=docker/dockerfile:1


#Calling from the python
FROM python:3.8

WORKDIR /app

#Copying the requirements.txt from the file 

COPY requirements.txt requirements.txt

#Now after downloading the requirements.txt file, installation takes place
RUN pip3 install -r requirements.txt

COPY . .


#Exposing the details on the port
EXPOSE 9000
CMD [ "python", "app.py"]
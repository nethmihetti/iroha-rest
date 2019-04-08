FROM ubuntu:latest
MAINTAINER Alex Tarasov "alxndrtarasov@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
#RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
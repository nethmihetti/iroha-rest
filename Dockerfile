FROM python:latest
MAINTAINER Marat Kashaev "mtkashaev@gmail.com"
COPY . /iroha-py
WORKDIR /iroha-py
RUN pip3 install flask
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
COPY . /geocoding
WORKDIR /geocoding
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["geocoding.py"]
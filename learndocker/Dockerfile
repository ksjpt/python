FROM ubuntu:20.04
USER root


RUN apt-get update
RUN apt-get install -y python3.9
RUN apt-get install -y python3-pip

COPY requirements.txt .
RUN python3.9 -m pip install -r requirements.txt

ENV SITE_DOMAIN=ksjpt.com

WORKDIR /var

ADD https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data .

COPY script.py .
ENTRYPOINT ["python3.9", "script.py"]

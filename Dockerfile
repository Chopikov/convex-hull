FROM ubuntu:20.04
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update
RUN apt-get install -y build-essential python3.8-dev gcc python3-pip
RUN apt-get install -y vim nano
RUN apt-get clean

COPY . /app
WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR /app/blist-py39
RUN python3 setup.py install

WORKDIR /app

CMD ["/bin/bash"]
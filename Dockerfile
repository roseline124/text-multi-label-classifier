FROM ubuntu:latest
LABEL maintainer="roseline124 <guseod24@gmail.com>"

ENV LANG=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
  apt-get install -y --no-install-recommends tzdata g++ curl

# install java
RUN apt-get install -y openjdk-8-jdk
ENV JAVA_HOME="/usr/lib/jvm/java-1.8-openjdk"

# install python
RUN apt-get install -y python3-pip python3-dev
RUN cd /usr/local/bin && \
  ln -s /usr/bin/python3 python && \
  ln -s /usr/bin/pip3 pip && \
  pip3 install --upgrade pip

# apt clean
RUN apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# copy source dest
COPY . .

# install python package
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

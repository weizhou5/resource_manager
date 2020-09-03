# https://github.com/zalando/connexion/issues/739
FROM harbor.eniot.io/envisioniot/python3

RUN mkdir -p /usr/src/app
RUN yum install -y python36-dbus
#RUN apk add py3-dbus
#RUN sed -i "s/archive.ubuntu.com/mirrors.aliyun.com/g" /etc/apt/sources.list && \
#    apt update && apt install -y libdbus-1-dev libglib2.0-dev
WORKDIR /usr/src/app

COPY . /usr/src/app/
RUN rm -rf /usr/src/app/config/*
COPY __main__.py  /usr/src/app/__main__.py
COPY requirements.txt  /usr/src/app/requirements.txt
#RUN pip3 install dbus-python
RUN yum install gcc g++ make libffi-dev openssl-dev python3-devel -y
RUN pip3 install --no-cache-dir -r requirements.txt


EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["__main__.py"]
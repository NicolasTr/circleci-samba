FROM phusion/baseimage:0.9.13

RUN apt-get update
RUN apt-get install -y python-pip smbclient
RUN pip install nose mock

ADD test_mount.py /tests/test_mount.py

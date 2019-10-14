FROM python:3.6.7-jessie
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN echo "deb http://mirrors.aliyun.com/debian jessie main contrib non-free\n   deb http://mirrors.aliyun.com/debian jessie-proposed-updates main contrib non-free\n  deb http://mirrors.aliyun.com/debian jessie-updates main contrib non-free" > /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        ldap-utils libldap2-dev libsasl2-dev
RUN pip install -r requirements.txt

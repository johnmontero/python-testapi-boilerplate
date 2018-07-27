FROM amazonlinux:2018.03

RUN yum -y update && yum -y install \
    python36 \
    python36-pip \
    python36-devel \
    zsh

ONBUILD ADD app /app/
WORKDIR /app

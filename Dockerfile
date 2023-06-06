FROM python:3
USER root
WORKDIR /root/

RUN apt-get update
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN pip install asana
RUN pip install python-dotenv
RUN pip install pytest
FROM python:3
USER root

RUN apt-get update
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN pip install --upgrade pip --proxy="http://proxy.uec.ac.jp:8080"
RUN pip install --upgrade setuptools --proxy="http://proxy.uec.ac.jp:8080"

RUN pip install asana --proxy="http://proxy.uec.ac.jp:8080"
RUN pip install python-dotenv --proxy="http://proxy.uec.ac.jp:8080"
RUN pip install pytest --proxy="http://proxy.uec.ac.jp:8080"
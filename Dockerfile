FROM python:latest

ADD ./requirements.txt /home/requirements.txt
RUN pip install -r /home/requirements.txt
RUN pip install pytest pytest-cov

COPY ./app /home/app/
COPY ./tests /home/tests/

WORKDIR /home

FROM python:3.9-bullseye

ADD ./requirements.txt /home/
RUN pip install -r /home/requirements.txt
RUN pip install pytest pytest-cov pyinstaller

WORKDIR /home

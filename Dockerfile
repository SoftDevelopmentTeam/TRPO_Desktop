FROM python:3.12.0-windowsservercore-ltsc2022

ADD ./requirements.txt /home/
RUN pip install -r /home/requirements.txt
RUN pip install pytest pytest-cov pyinstaller

WORKDIR /home

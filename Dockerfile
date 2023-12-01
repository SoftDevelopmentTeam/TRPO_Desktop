FROM python:3.12.0-windowsservercore-ltsc2022

ADD requirements.txt .
RUN pip install -r requirements.txt
RUN pip install pytest pytest-cov pyinstaller

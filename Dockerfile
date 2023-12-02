FROM python:3.9-bullseye

ADD requirements.txt .
RUN pip install -r requirements.txt
RUN pip install pytest pytest-cov pyinstaller

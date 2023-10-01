FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/project
COPY  project/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY project/ ./
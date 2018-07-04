FROM python:3.5.3

WORKDIR /app/

COPY requirements.txt /app/
RUN pip install -r ./requirements.txt

COPY main.py __init__.py /app/

# ENTRYPOINT /bin/bash
EXPOSE 5000

ENV ENVIRONMENT local

ENTRYPOINT python ./main.py
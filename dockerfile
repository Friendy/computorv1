FROM python:3.13-slim

WORKDIR /usr/src/

COPY ./app .
COPY ./run.sh .

CMD [ "bash"]
FROM python:3.13-slim

WORKDIR /usr/src/

COPY ./app .
COPY ./run-tests.sh .

CMD [ "bash"]
FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN apt-get install -y gdal-bin libgdal-dev

RUN mkdir /code
WORKDIR /code
COPY rtrw_serpong /code/
RUN pip install -r requirements.txt

# #RUN mkdir /olt_adapter_docker_certs
# #COPY ./olt_adapter_docker_certs /olt_adapter_docker_certs/

RUN pwd
RUN ls

ENTRYPOINT [ "/code/entrypoint.sh" ]

FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add gcc python3-dev musl-dev mariadb-dev build-base unixodbc-dev curl gnupg
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev

RUN mkdir /code
WORKDIR /code
COPY rtrw_serpong /code/
RUN pip install -r requirements.txt

# #RUN mkdir /olt_adapter_docker_certs
# #COPY ./olt_adapter_docker_certs /olt_adapter_docker_certs/

# RUN pwd
# RUN ls

# WORKDIR /code/bizzydataoperation
# # COPY entrypoint.sh /code/
# # COPY entrypoint.dev.sh /code/
# # RUN python manage.py migrate guardian
# # RUN python manage.py migrate impersonate
# # RUN python manage.py migrate embedded
# # RUN echo yes | python manage.py collectstatic
# # ENTRYPOINT [ "/code/entrypoint.sh" ]

FROM harbor.eencloud.com/qa/een-web-qa:latest as een_web
FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED 1

#Install python stuff
WORKDIR /usr/src/app

COPY . .

# Adding the een_web dependencies
COPY --from=een_web /usr/src/app/een_web/. /usr/src/app/een_web

RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y \
    vim \
    procps \
    net-tools \
    curl

CMD ["python3", "/usr/src/app/manage.py", "runserver"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]

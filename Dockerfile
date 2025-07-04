FROM eclipse-mosquitto:latest

USER root
RUN apk add --no-cache gettext
USER mosquitto

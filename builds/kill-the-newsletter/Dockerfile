FROM debian:12

WORKDIR /kill-the-newsletter

RUN apt update
RUN apt install -y wget

RUN wget https://github.com/leafac/kill-the-newsletter/releases/download/v1.0.1/kill-the-newsletter--linux--v1.0.1.tgz

RUN tar -xzf kill-the-newsletter--linux--v1.0.1.tgz

COPY docker.js .

CMD ["./kill-the-newsletter", "docker.js"]

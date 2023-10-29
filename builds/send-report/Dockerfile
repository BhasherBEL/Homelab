FROM alpine:latest

RUN apk --no-cache add curl mutt

COPY send.sh /usr/local/bin/send.sh
COPY init.sh /usr/local/bin/init.sh

RUN chmod +x /usr/local/bin/send.sh /usr/local/bin/init.sh

CMD ["/usr/local/bin/init.sh"]
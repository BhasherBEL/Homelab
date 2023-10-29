#!/bin/sh

CRON_SCHEDULE=${CRON_SCHEDULE:-"0 2 * * 0"}

echo "$CRON_SCHEDULE /usr/local/bin/send.sh" > /etc/crontabs/root

echo "Service ready on schedule $CRON_SCHEDULE"

crond -f

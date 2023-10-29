#!/bin/sh

TMP_PDF="/tmp/report.pdf"

curl -o "$TMP_PDF" "$PDF_URL"

if [ $? -eq 0 ]; then
  echo "Sending the report as an attachment" | mutt -s "Weekly Report" -e "set smtp_url=smtps://${SMTP_USER}:${SMTP_PASSWORD}@${SMTP_SERVER}:${SMTP_PORT}" -e 'set from="${FROM}"' -a "$TMP_PDF" -- "${TO_EMAIL}" 

  if [ $? -eq 0 ]; then
    echo "Email sent successfully"
  else
    echo "Failed to send the email"
  fi
else
  echo "Failed to download the PDF"
fi

rm -f "$TMP_PDF"

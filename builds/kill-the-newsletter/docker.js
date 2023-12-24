module.exports = async (require) => {
    const path = require("path");
    const killTheNewsletter = require(".").default;

    const { webApplication, emailApplication } = killTheNewsletter(
        path.join("/data")
    );

    webApplication.set("url", process.env.URL || "http://localhost");
    webApplication.set("email", process.env.SMTP || "smtp://localhost");
    webApplication.set("administrator", `mailto:${process.env.ADMIN_EMAIL || "localhost"}`);


    webApplication.listen(80, () => {
        console.log("Kill-the-newsletter server started");
        console.log(webApplication.get("url"));
    });

    emailApplication.listen(25, () => {
        console.log("Email server started");
    });

    const Imap = require('imap');
    const nodemailer = require('nodemailer');
    const { simpleParser } = require('mailparser');

    const imapConfig = {
        user: process.env.IMAP_USER,
        password: process.env.IMAP_PASSWORD,
        host: process.env.IMAP_HOST,
        port: process.env.IMAP_PORT,
        tls: true
    };

    const smtpConfig = {
        host: 'localhost',
        port: 25,
        secure: false
    };

    const imap = new Imap(imapConfig);

    function openInbox(cb) {
        imap.openBox('INBOX', false, cb);
    }

    function processEmails() {
        openInbox((err, box) => {
            if (err) throw err;

            imap.search(['UNSEEN'], (err, results) => {
                if (err || !results || !results.length) {
                    console.log('No new emails');
                    return;
                }

                const f = imap.fetch(results, { bodies: '' });
                f.on('message', msg => {
                    msg.on('body', stream => {
                        simpleParser(stream, async (err, mail) => {
                            let transporter = nodemailer.createTransport(smtpConfig);

                            await transporter.sendMail({
                                from: mail.from,
                                to: mail.to,
                                subject: mail.subject,
                                text: mail.text,
                                html: mail.html
                            });

                            console.log('Email forwarded');
                        });
                    });
                });
            });
        });
    }

    imap.once('ready', () => {
        processEmails();

        setInterval(processEmails, (proess.env.INTERVAL || 300) * 1000);
    });
    imap.once('error', err => console.error(err));
    imap.connect();

};
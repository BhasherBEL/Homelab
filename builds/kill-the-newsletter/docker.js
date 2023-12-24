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

};

import dotenv
import smtplib
from email.message import EmailMessage




def send_email(msg:str) -> None:

    FROM = dotenv.get_key("./.env", "FROM")
    TO = dotenv.get_key("./.env", "TO")
    PASS = dotenv.get_key("./.env", "PASS")


    subject = "Tickers"

    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = FROM
    message['To'] = TO
    message.set_content(msg)

    smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)
    smtp.starttls()
    smtp.login(user=FROM, password=PASS)
    smtp.send_message(message)
    smtp.quit()




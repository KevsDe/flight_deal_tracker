import dotenv
import os
import smtplib
dotenv.load_dotenv(dotenv.find_dotenv())
MY_EMAIL = os.environ.get("MY_EMAIL")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
DESTINATION_EMAIL = os.environ.get("DESTINATION_EMAIL")


def send_email(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=DESTINATION_EMAIL, msg=message)


if __name__ == '__main__':
    send_email()
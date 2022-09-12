import smtplib
import datetime as d
import random

email_quote = []


class EmailBot:
    def __init__(self):
        pass


def read():
    with open("quotes.txt") as q:
        lines = q.readlines()
        email_quote.append(random.choice(lines))


def send_email(quote):
    my_email = "YOUR_USERNAME"
    password = "YOUR_PASSWORD"
    with smtplib.SMTP("Your Email Smtp, port = ) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=f"Receipients_Email",
                            msg=f"Subject: Weekly Quote\n\n{quote}")
        connection.close()


now = d.datetime.now()
day_of_week = now.weekday()
if day_of_week == 6:
    read()
    quote = email_quote
    send_email(quote)

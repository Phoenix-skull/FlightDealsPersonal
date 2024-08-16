import os
import smtplib

# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        self.email = os.environ['EMAIL']
        self.password = os.environ['APP_PASSWORD']

    def send_msg(self, price, destination, out_date, return_date):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.starttls()
            smtp.login(user=self.email, password=self.password)
            smtp.sendmail(from_addr=self.email,
                          to_addrs=self.email,
                          msg= (f"Subject: Low price alert! \n\n Only £{price} to fly"
               f" to {destination}, on {out_date} until {return_date}.").encode())

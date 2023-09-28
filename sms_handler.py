import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

class SMSHandler:
    def __init__(self):
        self.sms_config = {
            "account_sid": os.environ.get("ACCOUNT_SID"),
            "auth_token": os.environ.get("AUTH_TOKEN"),
            "twilio_phone": os.environ.get("TWILIO_PHONE_NUMBER"),
            "my_phone": os.environ.get("MY_PHONE_NUMBER")
        }
        for key, value in self.sms_config.items():
            assert value is not None, f"Environment variable for {key} is not set!"
    
    def send_sms(self, message):
        try:
            client = Client(self.sms_config["account_sid"], self.sms_config["auth_token"])
            client.messages.create(
                body=message,
                from_=self.sms_config["twilio_phone"],
                to=self.sms_config["my_phone"]
            )
        except Exception as e:
            print(f"Error sending SMS: {e}")

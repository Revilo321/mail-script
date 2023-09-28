import os
import imaplib
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from dotenv import load_dotenv
load_dotenv()

ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
MY_PHONE_NUMBER = os.environ.get('MY_PHONE_NUMBER')

EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')
IMAP_SERVER = os.environ.get('IMAP_SERVER')
SEARCH_SENDER = os.environ.get('SEARCH_SENDER')

def check_for_email():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL, PASSWORD)
        mail.select('inbox')

        _, email_ids = mail.search(None, f'(FROM "{SEARCH_SENDER}")', '(UNSEEN)', f'(BODY "test")')

        if email_ids[0]:
            print('found email')
            """ send_sms() """

        mail.logout()

    except imaplib.IMAP4.error as e:
        print(f"IMAP error: {e}")
    except Exception as e:
        print(f"Error while checking email: {e}")

def send_sms():
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=f"Du har modtaget en email om studiekontrol fra: {SEARCH_SENDER}",
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE_NUMBER
        )

    except TwilioRestException as e:
        print(f"Twilio error: {e}")
    except Exception as e:
        print(f"Error while sending SMS: {e}")

if __name__ == "__main__":
    check_for_email()
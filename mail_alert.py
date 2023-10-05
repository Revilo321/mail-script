import os
import logging
from email_handler import EmailHandler
from sms_handler import SMSHandler
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)

def main():
    EMAIL_MESSAGE = os.environ.get('EMAIL_MESSAGE')
    try:
        email_handler = EmailHandler()
        sms_handler = SMSHandler()

        email_ids = email_handler.check_email_for_sender()
        if email_ids:
            logging.info(f"Found {len(email_ids)} new emails from target sender.")
            sms_handler.send_sms(f"{EMAIL_MESSAGE}")
            email_handler.mark_as_read(email_ids)
        else:
            logging.info("No new emails found from target sender.")
    except AssertionError as e:
        logging.error(f"Configuration Error: {e}")
    except Exception as e:
        logging.error(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()

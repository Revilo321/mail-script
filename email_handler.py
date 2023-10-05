import os
import imaplib
from dotenv import load_dotenv
load_dotenv()

class EmailHandler:
    def __init__(self):
        self.email_config = {
            "address": os.environ.get("EMAIL"),
            "password": os.environ.get("PASSWORD"),
            "imap_server": os.environ.get("IMAP_SERVER"),
            "search_sender": os.environ.get("SEARCH_SENDER")
        }
        for key, value in self.email_config.items():
            assert value is not None, f"Environment variable for {key} is not set!"
    
    
    def check_email_for_sender(self):
        email_ids = []
        TEXT_TO_FIND = os.environ.get("TEXT_TO_FIND")
        try:
            mail = imaplib.IMAP4_SSL(self.email_config["imap_server"])
            mail.login(self.email_config["address"], self.email_config["password"])
            mail.select('inbox')
            _, email_ids_bytes = mail.search(None, f'(FROM "{self.email_config["search_sender"]}")', '(UNSEEN)', f'(BODY {TEXT_TO_FIND})')
            email_ids = email_ids_bytes[0].decode('utf-8').split()
        except Exception as e:
            print(f"Error while checking email: {e}")
        return email_ids
    
    def mark_as_read(self, email_ids):
        try:
            mail = imaplib.IMAP4_SSL(self.email_config["imap_server"])
            mail.login(self.email_config["address"], self.email_config["password"])
            mail.select('inbox')
            for e_id in email_ids:
                mail.store(e_id, '+FLAGS', '\\Seen')
        except Exception as e:
            print(f"Error marking emails as read: {e}")

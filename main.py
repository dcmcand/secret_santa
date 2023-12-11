from os import path
import logging
import conf
from email_providers.mailgun import MailGunSender
from secret_santa.parser import parse_csv
from secret_santa.christmas import send_secret_santa


def main():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    file_path = path.abspath("./test-config.csv")
    participants = parse_csv(file_path)

    mailer = MailGunSender(
        email_domain=conf.EMAIL_DOMAIN,
        api_key=conf.MG_API_KEY,
        sender_email=conf.SENDER_EMAIL,
        sender_name=conf.SENDER_NAME
    )

    assignments = send_secret_santa(mailer, participants)

    for assignment in assignments:
        gifter, giftee = assignment
        logging.info(f"{gifter} gives to {giftee}")


if __name__ == "__main__":
    main()

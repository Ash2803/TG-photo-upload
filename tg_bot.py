import os

import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    tg_token = os.getenv('TG_BOT_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')
    bot = telegram.Bot(token=tg_token)
    bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")


if __name__ == '__main__':
    main()

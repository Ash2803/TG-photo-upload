import os
import random

import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    tg_token = os.getenv('TG_BOT_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')
    bot = telegram.Bot(token=tg_token)
    bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
    file_names = os.listdir('images')
    while True:
        with open(f'images/{random.choice(file_names)}', 'rb') as file:
            bot.send_photo(chat_id=chat_id, photo=file)


if __name__ == '__main__':
    main()

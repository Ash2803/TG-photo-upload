import argparse
import os
import random
import time

import telegram
from dotenv import load_dotenv


def posting_files(chat_id, tg_token, posting_time):
    bot = telegram.Bot(token=tg_token)
    files = os.listdir('images')
    random.shuffle(files)
    while True:
        for file_name in files:
            time.sleep(int(posting_time))
            with open(f'images/{file_name}', 'rb') as file:
                bot.send_photo(chat_id=chat_id, photo=file)


def main():
    load_dotenv()
    tg_token = os.getenv('TG_BOT_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')
    posting_time = os.getenv('POSTING_TIME')
    parser = argparse.ArgumentParser(
        description='Публикует фото в телеграм бота'
    )
    parser.add_argument('-t', '--posting_time', help='Кол-во времени задержки между публикациями', type=int)
    args = parser.parse_args()
    if args.posting_time:
        posting_files(chat_id, tg_token, args.posting_time)
    else:
        posting_files(chat_id, tg_token, posting_time)


if __name__ == '__main__':
    main()

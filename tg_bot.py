import argparse
import os
import random
import time
from pathlib import Path

import telegram
from dotenv import load_dotenv


def posting_files(chat_id, tg_token, posting_time):
    bot = telegram.Bot(token=tg_token)
    files = os.listdir('images')
    random.shuffle(files)
    image_dir_path = Path('images')
    while True:
        try:
            for file_name in files:
                time.sleep(posting_time)
                with open(image_dir_path / f'{file_name}', 'rb') as file:
                    bot.send_photo(chat_id=chat_id, photo=file)
        except telegram.error.NetworkError:
            print('Connection was lost')


def main():
    load_dotenv()
    tg_token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    parser = argparse.ArgumentParser(
        description='Публикует фото в телеграм бота'
    )
    parser.add_argument('-t', '--posting_time', help='Кол-во времени задержки между публикациями',
                        type=int, default=14400)
    args = parser.parse_args()
    posting_files(chat_id, tg_token, args.posting_time)


if __name__ == '__main__':
    main()

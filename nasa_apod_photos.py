import argparse
import os
import requests
from dotenv import load_dotenv
from download_photos import fetch_images


def download_nasa_photo(token, count, img_name):
    """Downloading NASA photos"""
    params = {
        'api_key': token,
        'count': count
    }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
    response.raise_for_status()
    images = filter(lambda img_key: img_key['media_type'] in 'image', response.json())
    urls = [url['url'] for url in images]
    fetch_images(urls, params, img_name)


def main():
    load_dotenv()
    nasa_apikey = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser(description='Скачивает APOD фото NASA')
    parser.add_argument('-c', '--count', help='Кол-во фото', type=int, default=10)
    args = parser.parse_args()
    download_nasa_photo(nasa_apikey, args.count, img_name='APOD_photo_')


if __name__ == '__main__':
    main()

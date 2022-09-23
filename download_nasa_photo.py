import argparse
import os
import requests
from dotenv import load_dotenv
from images_download import fetch_images


def download_nasa_photo(token, count):
    """Downloading NASA photos"""
    params = {
        'api_key': token,
        'count': count
    }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
    response.raise_for_status()
    key_value = 'image'
    images = filter(lambda img_key: img_key['media_type'] in key_value, response.json())
    urls = [url['url'] for url in images]
    print(urls)
    fetch_images(urls, params)


def main():
    load_dotenv()
    nasa_apikey = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser(description='Скачивает APOD фото NASA')
    parser.add_argument('-c', '--count', help='Кол-во фото', type=int, default=10)
    args = parser.parse_args()
    download_nasa_photo(nasa_apikey, args.count)


if __name__ == '__main__':
    main()

import os
import requests
from dotenv import load_dotenv
from images_download import fetch_images


def download_nasa_photo(token):
    """Downloading NASA photos"""
    param = {
        'api_key': token,
        'count': '41'
    }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=param)
    response.raise_for_status()
    key_value = 'image'
    images = list(filter(lambda img_key: img_key['media_type'] in key_value, response.json()))
    urls = []
    for url in images:
        urls.append(url['url'])
    fetch_images(urls)


def main():
    load_dotenv()
    nasa_apikey = os.environ['NASA_API_KEY']
    download_nasa_photo(nasa_apikey)


if __name__ == '__main__':
    main()

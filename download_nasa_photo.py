import os
from pathlib import Path

import requests
from dotenv import load_dotenv

from get_format import get_format


def download_nasa_photo(token):
    """Downloading NASA photos"""
    param = {
        'api_key': token,
        'count': '41'
    }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=param)
    response.raise_for_status()
    Path('images').mkdir(parents=True, exist_ok=True)
    for url_number, url in enumerate(response.json()):
        image = requests.get(url['url'])
        image.raise_for_status()
        file_format = get_format(url['url'])
        if not file_format:
            continue
        with open(f'images/nasa_{url_number}{file_format}', 'wb') as file:
            file.write(image.content)


def main():
    load_dotenv()
    nasa_apikey = os.getenv('NASA_API_KEY')
    download_nasa_photo(nasa_apikey)


if __name__ == '__main__':
    main()

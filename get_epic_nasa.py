import os
import requests
from dotenv import load_dotenv
from images_download import fetch_images
from datetime import datetime


def get_epic_nasa(token):
    """Downloading EPIC NASA photos"""
    param = {
        'api_key': token
    }
    response = requests.get('https://api.nasa.gov/EPIC/api/natural', params=param)
    response.raise_for_status()
    urls = []
    for link_number, link in enumerate(response.json(), start=1):
        image_name = link['image']
        a_date = datetime.fromisoformat(link['date'])
        image_date = f'{a_date.year}\{a_date.month}\{a_date.day}'
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png?api_key={token}'
        urls.append(image_url)
        fetch_images(urls)


def main():
    load_dotenv()
    nasa_apikey = os.environ['NASA_API_KEY']
    get_epic_nasa(nasa_apikey)


if __name__ == '__main__':
    main()

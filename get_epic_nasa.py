import os
import requests
from pathlib import Path
from dotenv import load_dotenv

from get_format import get_format


def get_epic_nasa(token):
    """Downloading EPIC NASA photos"""
    param = {
        'api_key': token
    }
    response = requests.get('https://api.nasa.gov/EPIC/api/natural?api_key=DEMO_KEY', params=param)
    response.raise_for_status()
    Path('images').mkdir(parents=True, exist_ok=True)
    for link_number, link in enumerate(response.json(), start=1):
        image_name = link['image']
        image_date = link['date'].split(" ")[0].replace('-', '/')
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png?api_key={token}'
        file_format = get_format(image_url)
        image = requests.get(image_url)
        image.raise_for_status()
        with open(f'images/nasa_epic_photo{link_number}{file_format}', 'wb') as file:
            file.write(image.content)


def main():
    load_dotenv()
    nasa_apikey = os.getenv('NASA_API_KEY')
    get_epic_nasa(nasa_apikey)


if __name__ == '__main__':
    main()

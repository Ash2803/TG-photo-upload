import requests
from pathlib import Path

from get_format import get_format


def fetch_images(urls, params):
    image_dir_path = Path('images')
    image_dir_path.mkdir(parents=True, exist_ok=True)
    for url_number, url in enumerate(urls):
        file_format = get_format(url)
        image = requests.get(url, params=params)
        image.raise_for_status()
        with open(image_dir_path / f'photo_{url_number}{file_format}', 'wb') as file:
            file.write(image.content)

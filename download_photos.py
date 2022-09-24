import os
import urllib.parse

import requests
from pathlib import Path


def fetch_images(urls, params, img_name):
    image_dir_path = Path('images')
    image_dir_path.mkdir(parents=True, exist_ok=True)
    for url_number, url in enumerate(urls):
        file_format = get_images_format(url)
        image = requests.get(url, params=params)
        image.raise_for_status()
        with open(image_dir_path / f'{img_name}{url_number}{file_format}', 'wb') as file:
            file.write(image.content)


def get_images_format(photo_url):
    split_url = urllib.parse.urlsplit(photo_url)
    split_domain = urllib.parse.unquote(split_url[2])
    file_format = os.path.splitext(split_domain)
    if file_format[1]:
        return file_format[1]

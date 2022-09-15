import requests
import argparse
from pathlib import Path

from get_format import get_format


def fetch_spacex_last_launch(launch_id):
    """Get photos of the last SpaceX rocket launch"""
    if launch_id:
        response = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}')
        response.raise_for_status()
    else:
        response = requests.get('https://api.spacexdata.com/v5/launches/latest')
        response.raise_for_status()
    urls = response.json()['links']['flickr']['original']
    if not urls:
        print('Sorry, there are no photos from the latest launch yet!')
    Path('images').mkdir(parents=True, exist_ok=True)
    for url_number, url in enumerate(urls):
        file_format = get_format(url)
        image = requests.get(url)
        image.raise_for_status()
        with open(f'images/spacex_{url_number}{file_format}', 'wb') as file:
            file.write(image.content)


def main():
    parser = argparse.ArgumentParser(
        description='Скачивает фото запуска ракет'
                    ' SpaceX'
    )
    parser.add_argument('-l', '--launch_id', help='ID запуска')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch_id)


if __name__ == '__main__':
    main()

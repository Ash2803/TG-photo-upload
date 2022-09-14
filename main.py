import os
import urllib.parse
import requests
from pathlib import Path
from dotenv import load_dotenv


def fetch_spacex_last_launch(launch_id, path):
    """Get photos of the last SpaceX rocket launch"""
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}')
    response.raise_for_status()
    urls = response.json()['links']['flickr']['original']
    Path(path).mkdir(parents=True, exist_ok=True)
    for url_number, url in enumerate(urls):
        file_format = get_format(url)
        image = requests.get(url)
        image.raise_for_status()
        with open(f'{path}/spacex_{url_number}{file_format}', 'wb') as file:
            file.write(image.content)


def download_nasa_photo(token, path):
    """Downloading NASA photos"""
    param = {
        'api_key': token,
        'count': '40'
    }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=param)
    response.raise_for_status()
    Path(path).mkdir(parents=True, exist_ok=True)
    for url_number, url in enumerate(response.json()):
        image = requests.get(url['url'])
        image.raise_for_status()
        file_format = get_format(url['url'])
        if not file_format:
            continue
        with open(f'{path}/nasa_{url_number}{file_format}', 'wb') as file:
            file.write(image.content)


def get_epic_nasa(token, path):
    """Downloading EPIC NASA photos"""
    param = {
        'api_key': token
    }
    response = requests.get('https://api.nasa.gov/EPIC/api/natural?api_key=DEMO_KEY', params=param)
    response.raise_for_status()
    Path(path).mkdir(parents=True, exist_ok=True)
    for link_number, link in enumerate(response.json(), start=1):
        image_name = link['image']
        image_date = link['date'].split(" ")[0].replace('-', '/')
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png?api_key={token}'
        file_format = get_format(image_url)
        image = requests.get(image_url)
        image.raise_for_status()
        with open(f'{path}/nasa_epic_photo{link_number}{file_format}', 'wb') as file:
            file.write(image.content)


def get_format(photo_url):
    url_split = urllib.parse.urlsplit(photo_url)
    domain_split = urllib.parse.unquote(url_split[2])
    get_file_format = os.path.splitext(domain_split)
    if get_file_format[1]:
        return get_file_format[1]


def main():
    launch_id = input('Enter launch id: ')
    path = input('Enter download path: ')
    fetch_spacex_last_launch(launch_id, path)
    load_dotenv()
    nasa_apikey = os.getenv('NASA_API_KEY')
    download_nasa_photo(nasa_apikey, path)
    get_epic_nasa(nasa_apikey, path)


if __name__ == '__main__':
    main()

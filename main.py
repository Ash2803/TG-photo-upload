import os
import urllib.parse
import requests
from pathlib import Path
from dotenv import load_dotenv


def file_download(path, url):
    """Download files to user created directory"""
    response = requests.get(url)
    response.raise_for_status()
    Path(path).mkdir(parents=True, exist_ok=True)
    with open(f'{path}/hubble.jpeg', 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(launch_id, path):
    """Get photos of the last SpaceX rocket launch"""
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}')
    response.raise_for_status()
    urls = response.json()['links']['flickr']['original']
    Path(path).mkdir(parents=True, exist_ok=True)
    for url_number, url in enumerate(urls):
        image = requests.get(url)
        image.raise_for_status()
        with open(f'{path}/spacex_{url_number}.jpeg', 'wb') as file:
            file.write(image.content)


def get_nasa_photo(token, nasa_url):
    links = []
    payload = {
        'api_key': token,
        'count': '40'
    }
    response = requests.get(nasa_url, params=payload)
    response.raise_for_status()
    for link in response.json():
        links += link['hdurl']
    return links


def refactoring_nasa_photo(photo_url):
    url_split = urllib.parse.urlsplit(photo_url)
    domain_split = urllib.parse.unquote(url_split[2])
    get_file_format = os.path.splitext(domain_split)
    return get_file_format[1]
    # return url_split


def main():
    # url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    # file_download(path, url)
    # launch_id = input('Enter launch id: ')
    # path = input('Enter download path: ')
    # fetch_spacex_last_launch(launch_id, path)
    load_dotenv()
    nasa_url = input('Enter url: ')
    nasa_apikey = os.getenv('NASA_API_KEY')
    nasa_photo_url = get_nasa_photo(nasa_apikey, nasa_url)
    print(nasa_photo_url)
    # print(refactoring_nasa_photo(nasa_photo_url))


if __name__ == '__main__':
    main()

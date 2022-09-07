import requests
from pathlib import Path


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


def main():
    # url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    # file_download(path, url)
    launch_id = input('Enter launch id: ')
    path = input('Enter download path: ')
    fetch_spacex_last_launch(launch_id, path)


if __name__ == '__main__':
    main()

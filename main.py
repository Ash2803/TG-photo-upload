import requests
from pathlib import Path


def file_download(path, url):
    """Download files to user created directory"""
    headers = {
        'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    Path(path).mkdir(parents=True, exist_ok=True)
    with open(f'{path}/hubble.jpeg', 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(launch_id):
    """Get photos of the last SpaceX rocket launch"""
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}')
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def main():
    path = input()
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    file_download(path, url)
    launch_id = input()
    print(fetch_spacex_last_launch(launch_id))


if __name__ == '__main__':
    main()

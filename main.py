import requests
from pathlib import Path


def file_download(filename, url):
    response = requests.get(url)
    response.raise_for_status()
    Path('images').mkdir(parents=True, exist_ok=True)
    with open(f'images/{filename}', 'wb') as file:
        file.write(response.content)


def main():
    filename = 'hubble.jpeg'
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    file_download(filename, url)


if __name__ == '__main__':
    main()

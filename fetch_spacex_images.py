import requests
import argparse

from download_photos import fetch_images


def fetch_spacex_last_launch(launch_id, img_name):
    """Get photos of the last SpaceX rocket launch"""
    params = {}
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}')
    response.raise_for_status()
    urls = response.json()['links']['flickr']['original']
    if urls:
        return fetch_images(urls, params, img_name)
    else:
        print('Sorry, there are no photos from the latest launch yet!')


def main():
    parser = argparse.ArgumentParser(
        description='Скачивает фото запуска ракет'
                    ' SpaceX'
    )
    parser.add_argument('-l', '--launch_id', help='ID запуска', default='latest')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch_id, img_name='spacex_')


if __name__ == '__main__':
    main()

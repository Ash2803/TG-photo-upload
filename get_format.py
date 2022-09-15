import os
import urllib.parse


def get_format(photo_url):
    url_split = urllib.parse.urlsplit(photo_url)
    domain_split = urllib.parse.unquote(url_split[2])
    get_file_format = os.path.splitext(domain_split)
    if get_file_format[1]:
        return get_file_format[1]


def main():
    pass


if __name__ == '__main__':
    main()

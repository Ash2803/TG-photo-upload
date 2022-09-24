import os
import urllib.parse


def get_format(photo_url):
    splitted_url = urllib.parse.urlsplit(photo_url)
    splitted_domain = urllib.parse.unquote(splitted_url[2])
    file_format = os.path.splitext(splitted_domain)
    if file_format[1]:
        return file_format[1]

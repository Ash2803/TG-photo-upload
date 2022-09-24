import os
import urllib.parse


def get_format(photo_url):
    split_url = urllib.parse.urlsplit(photo_url)
    split_domain = urllib.parse.unquote(split_url[2])
    file_format = os.path.splitext(split_domain)
    if file_format[1]:
        return file_format[1]

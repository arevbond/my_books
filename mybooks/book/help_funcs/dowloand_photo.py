from google_images_search import GoogleImagesSearch
from random import randint
import os
from django.conf import settings


def dowloand_photo(title: str, author: str):
    name_of_file = f'{title}-{author}'
    media_root = '/mnt/disk_d/django_projects/MyBooks/mybooks/media'
    path_to = media_root + '/covers/'
    # path_to = settings.MEDIA_ROOT + '/covers/'

    if os.path.exists(f'{path_to}{name_of_file}.png'):
        return f'/covers/{name_of_file}.png'

    gis = GoogleImagesSearch('AIzaSyAeTGAvY7IuqzxuI3tvlC1TVM1LcGMFbZc', 'c4cca0099d4394a26')

    _search_paramas = {
        'q': f'Обложка книги {title} {author}',
        'num': 1,
        'fileType': 'png',
        'imgSize': 'large',
        'stop': 1
    }

    gis.search(search_params=_search_paramas, path_to_dir=path_to, custom_image_name=name_of_file)
    print(f'{path_to}{name_of_file}.png')
    return f'/covers/{name_of_file}.png'
dowloand_photo('Сто лет одиночества', 'Габриель гарсия маркес')
# dowloand_photo('Мастер и Маргарита', 'Достоевский')
# dowloand_photo('Метро 2033',)

import os
import time
from pathlib import Path

from flickr_parser.parser import get_urls
from flickr_parser.downloader import download_images


# CHANGE ME
tags = ['girl sunglasses', 'guy sunglasses', 'person sunglasses']
max_amount = 1000
dst_dir = 'Downloads/flickr_data/'


def download(folder):
    '''
    :return nothing but downloads images
    '''
    counter = 0

    for tag in tags:
        urls = get_urls(image_tag=tag,
                        max_amount=max_amount)
        path = os.path.join(folder, tag)
        counter += download_images(urls, path, counter)

        if counter >= max_amount:
            return


if __name__ == '__main__':
    start_time = time.time()
    download(os.path.join(str(Path.home()), dst_dir))
    print(f'Parsing took {round(time.time() - start_time, 2)} seconds.')

import os
import requests

from find_face_with_glasses.face_detector import is_one_and_suitable


def create_folder(path):
    '''
    :param path: to target folder
    :return: nothing, but create folder if it not exists
    '''
    if not os.path.isdir(path):
        os.makedirs(path)


def download_images(urls, path, counter):
    """
    :param urls: list of target urls
    :param path: to write file
    :param counter: of downloaded images
    :return counter: of downloaded files
    """

    create_folder(path)

    for url in urls:
        img_name = url.split('/')[-1]  # take the last part of url
        img_path = os.path.join(path, img_name)

        if not os.path.isfile(img_path):  # ignore if already downloaded
            response = requests.get(url, stream=True)

            # write file to disk
            with open(img_path, 'wb') as f:
                f.write(response.content)

                # pass image filter
                if not is_one_and_suitable(img_path):
                    os.remove(img_path)

        # increase counter
        if os.path.isfile(img_path):
            counter += 1

    return counter

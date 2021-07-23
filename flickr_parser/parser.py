import os
import dotenv
from flickrapi import FlickrAPI


def get_photos(image_tag):
    '''
    :param image_tag: search images by this tag
    :return photos: iterable object
    '''
    extras = ','.join(SIZES)
    flickr = FlickrAPI(KEY, SECRET)
    photos = flickr.walk(text=image_tag,
                         extras=extras,  # find best resolution
                         privacy_filter=1,  # search only for public photos
                         per_page=50,
                         sort='relevance')  # find tagged targets first
    return photos


def get_url(photo):
    '''
    :param photo: target photo
    :return url: of target photo with largest resolution
    '''
    for i in range(len(SIZES)):
        url = photo.get(SIZES[i])
        if url:  # make sure this size exists
            return url


def get_urls(image_tag, max_amount):
    '''
    :param image_tag: search images by this tag
    :param max_amount: amount of photos you want
    :return urls: list of target urls
    '''
    photos = get_photos(image_tag)
    counter = 0
    urls = []
    for photo in photos:
        if counter < max_amount:
            url = get_url(photo)
            if url:
                urls.append(url)
                counter += 1
        else:
            break
    return urls


dotenv.load_dotenv('../.env')

# set api params
KEY = os.getenv('KEY')
SECRET = os.getenv('SECRET')

# list of sizes in order of preference
SIZES = ["url_o", "url_k", "url_h", "url_l", "url_c"]

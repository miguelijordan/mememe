import urllib.request
import re

# m3 modules
from me3.core.meme import Meme
import me3.core.me3_id_generator as me3_id_generator

# CONSTANTS
MEME_FOLDER = 'StuffMemes/'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
HEADERS = {'User-Agent': USER_AGENT}

RE_IMG_TAG = re.compile(r'<img([^>]+)/>')
RE_IMG_SRC_TAG = re.compile(r'src="([^"]+)"')
RE_EXTENSION = re.compile(r'(\.[^.?]+)')
EXTENSIONS = ('.jpg', '.jpeg' '.png', '.tif', '.gif')


def get_images_url_from_webpage(url):
    """ Obtain the url of all the images from the specified url webpage. """
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        webpage = urllib.request.urlopen(req).read()

        result = re.findall(RE_IMG_TAG, str(webpage))
        images = []
        for r in result:
            src = re.search(RE_IMG_SRC_TAG, r)
            if src is not None:
                image_url = src.group(1)
                images.append(image_url)
                #if image_url.endswith(EXTENSIONS):
                #    images.append(image_url)
        return images
    except:
        print("Error: " + url)
        return []

def download_meme(url):
    """ Download the image of the meme and retun its metadata. """
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        image = urllib.request.urlopen(req).read()

        meme_id = me3_id_generator.generate_id(image)
        extension = [e for e in EXTENSIONS if e in url]
        if extension == []:
            return None
        meme_path = MEME_FOLDER + str(meme_id) + extension[0]

        f = open(meme_path, "wb")
        f.write(image)
        f.close()

        meme = Meme(meme_id, meme_path)
        return meme
    except:
        return None

class MemeGetter:
    """ Generic Getter to obtain memes from Internet """

    def __init__(self, source_url):
        self.source_url = source_url

    def downloadMemes(self):
        images_url = get_images_url_from_webpage(self.source_url)
        #print(self.source_url + ' -> ' + str(len(images_url)))
        memes = []
        for i in images_url:
            #print(i)
            m = download_meme(i)
            if m is not None:
                if not m in memes:
                    m.source = self.source_url
                    memes.append(m)
        return memes

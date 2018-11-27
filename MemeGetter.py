import urllib.request
import re
import json
import Meme

# CONSTANTS
MEMES_FILE = 'raw_memes.dat'
MEME_FOLDER = 'memes/'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
HEADERS = {'User-Agent': USER_AGENT}

RE_IMG_TAG = re.compile(r'<img([^>]+)/>')
RE_IMG_SRC_TAG = re.compile(r'src="([^"]+)"')
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
                if image_url.endswith(EXTENSIONS):
                    images.append(image_url)
        return images
    except:
        return []

def download_meme(url):
    """ Download the image of the meme and retun its metadata. """
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        image = urllib.request.urlopen(req).read()

        meme_id = hash(image)
        extension = url[url.rfind('.'):]
        meme_path = MEME_FOLDER + str(meme_id) + extension

        f = open(meme_path, "wb")
        f.write(image)
        f.close()

        meme = Meme.Meme(meme_id, meme_path)
        return meme
    except:
        return None

def register_memes(memes):
    """ Write the memes' metadata in a JSON file """
    json.dump(memes, open(MEMES_FILE, 'w+'), cls=Meme.MemeJSONEncoder, sort_keys=True, indent=2)

class MemeGetter:
    """ Generic Getter to obtain memes from Internet """

    def __init__(self, source_url):
        self.source_url = source_url

    def downloadMemes(self):
        images_url = get_images_url_from_webpage(self.source_url)
        memes = []
        for i in images_url:
            m = download_meme(i)
            if m is not None:
                m.source = self.source_url
                memes.append(m)
        return memes

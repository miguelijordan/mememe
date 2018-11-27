import json
import random

# CONSTANTS
MEMES_FILE = 'memes.dat'

def load_memes():
    return json.load(open(MEMES_FILE))

class MemeDispatcher:

    def __init__(self):
        self.memes = load_memes()

    def getmeme(self, meme_id):
        try:
            meme = next((x for x in self.memes if x.id == meme_id), None)
            if meme is None:
                return None
            else:
                return meme.url
        except:
            return None

    def getmemeuser(self, user_id):
        try:
            meme = random.sample(self.memes, 1)[0]
            meme_json = json.dumps(meme, cls=Meme.MemeJSONEncoder, sort_keys=True, indent=2)
            return meme_json
        except:
            return None

    def putmemelike(self, user_id, meme_id, likeable):
        pass

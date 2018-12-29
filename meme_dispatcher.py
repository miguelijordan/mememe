import json
import random
import me3.core.me3_persistence as me3_persistence

# CONSTANTS
MEMES_FILE = 'StuffMemes.dat'
USERS_FILE = "Users.dat"


class MemeDispatcher:
    def __init__(self):
        list_of_memes = me3_persistence.load_memes(MEMES_FILE)
        self.memes = {}
        for m in list_of_memes:
            self.memes[m.id] = m

    def getmeme(self, meme_id):
        try:
            #meme = next((x for x in self.memes if x.id == meme_id), None)
            meme = self.memes[meme_id]
            if meme is None:
                return None
            else:
                return meme.url
        except:
            return None

    def getmemeuser(self, user_id):
        try:
            meme = self.memes[random.sample(list(self.memes), 1)[0]]
            meme_json = me3_persistence.meme_to_json(meme)
            return meme_json
        except:
            return None

    def putmemelike(self, user_id, meme_id, likeable):
        pass


# Tests
# memes = load_memes()
# print(str(len(memes)))
# unique_memes = set(memes)
# print(str(len(unique_memes)))
#memes.sort(key=lambda x : x.datetime)

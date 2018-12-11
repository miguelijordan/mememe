import json
import random
import Meme

# CONSTANTS
MEMES_FILE = 'memes.dat'

def load_memes():
    return json.load(open(MEMES_FILE), cls=Meme.MemeJSONDecoder)

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


def execution_time(stmt, ntimes):
    import timeit
    t = timeit.Timer(stmt=stmt, globals=globals())
    res = t.repeat(repeat=ntimes, number=1)
    return res

def execution_time_ms(stmt, ntimes):
    import statistics
    res = execution_time(stmt, ntimes)
    print("Code: " + stmt)
    print("Mean: " + str(statistics.mean(res) * 1e+3))
    print("Standard deviation: " + str(statistics.stdev(res) * 1e+3))
    print("Median: " + str(statistics.median(res) * 1e+3))


execution_time_ms("1+1", 1000)

memes = load_memes()
m = memes[0]
f = open(m.url, 'rb')
data = f.read()
f.close()

print(str(len(data)) + ' bytes.')
print(str(len(data)/1024) + ' kb.')

# print(str(len(memes)))
# unique_memes = set(memes)
# print(str(len(unique_memes)))
#memes.sort(key=lambda x : x.datetime)

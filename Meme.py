import datetime
import json

class Meme:
    """ Meme class """
    def __init__(self, url, source):
        self.datetime = datetime.datetime.now().isoformat()
        self.url = url
        self.source = source
        self.description = ""
        self.id = self.source + '_' + self.datetime

    def __repr__(self):
        return str(self.__dict__)

class MemeJSONEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


    #def toJSON(self):
    #    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


# m = Meme("G:\My Drive\Programming\Python\me3\memes", "Cabronazi")
# m2 = Meme("C:/meme2.jpg", "HumorLamentable")
#
# list = [m,m2]
# print(list)
#
# json.dump(list, open('memes.dat', 'w'), cls=MemeJSONEncoder, sort_keys=True, indent=2)
# print(open('memes.dat').read())
# print(json.load(open('memes.dat')))

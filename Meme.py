import datetime
import json

class Meme:
    """ Meme class """
    def __init__(self, id, url):
        self.datetime = datetime.datetime.now().isoformat()
        self.id = id
        self.url = url
        self.source = ""
        self.description = ""

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        if isinstance(other, Meme):
            return self.id == other.id
        return False

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

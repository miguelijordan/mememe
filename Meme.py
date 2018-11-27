import datetime
import json

class Meme:
    """ Meme class """
    def __init__(self, id, url):
        self.datetime = datetime.datetime.now().isoformat()
        self.id = str(id)
        self.url = url
        self.source = ""
        self.description = ""

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        if isinstance(other, Meme):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

class MemeJSONEncoder(json.JSONEncoder):
    """ Custom JSON Encoder for Meme class """
    def default(self, o):
        return o.__dict__

class MemeJSONDecoder(json.JSONDecoder):
    """ Custom JSON Decoder for Meme class """
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook)

    def object_hook(self, obj):
        meme = Meme(obj['id'], obj['url'])
        meme.datetime = obj['datetime']
        meme.description = obj['description']
        meme.source = obj['source']
        return meme

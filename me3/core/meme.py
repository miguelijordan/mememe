import datetime

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

    def __hash__(self):
        return hash(self.id)

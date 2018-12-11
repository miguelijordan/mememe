# -*- coding: utf-8 -*-
"""This module manage the persistence of the memes."""

import json
from me3.core.meme import Meme

def register_memes(memes, filename):
    """Save the memes' metadata in a JSON file."""
    json.dump(memes, open(filename, 'w+'), cls=MemeJSONEncoder, sort_keys=True, indent=2)

def load_memes(filename):
    return json.load(open(filename), cls=MemeJSONDecoder)

def meme_to_json(meme):
    return json.dumps(meme, cls=MemeJSONEncoder, sort_keys=True, indent=2)

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

# -*- coding: utf-8 -*-
"""This module generates unique IDs for memes."""

import hashlib

def generate_id(image):
    """Generate an ID for the meme from its image data bytes."""
    return hashlib.sha1(image).hexdigest()

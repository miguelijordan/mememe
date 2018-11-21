#!/usr/bin/env python3

"""
Mememe HTTP server.

Usage::
    ./m3-httpServer.py
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import Meme
import json

# CONSTANTS
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 8081

# Paths
# GET /user/<<userID>>/meme
PATH_MEME_DATA_STARTS = '/user/'
PATH_MEME_DATA_ENDS = '/meme'
# GET /meme/<<memeID>>
PATH_MEME_IMAGE = '/meme/'
# PUT /user/<<userID>>/meme/<<memeID>>/like|dislike
PATH_USER_LIKE = '/user/'

# MEME DE PRUEBA
MEME_PRUEBA = Meme.Meme("G:\My Drive\Programming\Python\me3\memes\drenaje.png", "Cabronazi")

# HTTPRequestHandler class
class m3HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        #logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))

        # GET /user/<<userID>>/meme
        if self.path.startswith(PATH_MEME_DATA_STARTS) and self.path.endswith(PATH_MEME_DATA_ENDS):
            meme_id = self.path[len(PATH_MEME_DATA_STARTS) : -len(PATH_MEME_DATA_ENDS)]

            logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))

            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()

            meme_json = json.dumps(MEME_PRUEBA, cls=Meme.MemeJSONEncoder, sort_keys=True, indent=2)
            self.wfile.write(meme_json.encode("UTF-8"))

            return

        # GET /meme/<<memeID>>
        if self.path.startswith(PATH_MEME_IMAGE):
            meme_id = self.path[len(PATH_MEME_IMAGE):]

            if meme_id != MEME_PRUEBA.id:
                print("error 1")
                return self.send_error(404)

            self.send_response(200)
            self.send_header('Content-type','image/png')
            self.end_headers()

            #logging.info("Requestline:\n%s\nSize (b): %i\n", str(self.requestline), sys.getsizeof(self.requestline))
            #logging.info("Requestline:\n%s\nSize (b): %i\n", str(self.requestline), len(bytes(str(self.requestline), "UTF-8")))
            #logging.info("Headers:\n%sSize (b): %i\n", str(self.headers), sys.getsizeof(self.headers))
            #logging.info("Headers:\n%sSize (b): %i\n", str(self.headers), len(bytes(str(self.headers), "UTF-8")))

            f = open(MEME_PRUEBA.url, 'rb')
            self.wfile.write(f.read())
            f.close()

            return

        # Error
        print("error 2")
        return self.send_error(400)

def run():
    # Server settings
    print('m3>Starting HTTP server...')
    server_address = (SERVER_ADDRESS, SERVER_PORT)
    httpd = HTTPServer(server_address, m3HTTPServer_RequestHandler)
    print('m3>Running HTTP server...')
    httpd.serve_forever()

if __name__ == '__main__':
    logging.basicConfig(filename='info.log', filemode='w', level=logging.INFO)
    run()
    #from sys import argv

    #if len(argv) == 2:
    #    run(port=int(argv[1]))
    #else:
    #    run()

#!/usr/bin/env python3

"""
Mememe HTTP server.

Usage::
    ./m3-httpServer.py
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import re
import meme_dispatcher

# CONSTANTS
SERVER_ADDRESS = '0.0.0.0'
SERVER_PORT = 8888

# Regex for API REST
RE_GET_MEMEDATA = re.compile(r'/user/([^/]+)/meme')
RE_GET_MEMEIMAGE = re.compile(r'/meme/([^/]+)')
RE_PUT_MEMELIKE = re.compile(r'/user/([^/]+)/meme/([^/]+)/([like|dislike])')

meme_dispatcher = meme_dispatcher.MemeDispatcher()

# HTTPRequestHandler class
class Me3HTTPRequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        #logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        try:
            result = RE_GET_MEMEDATA.match(self.path)
            if result is not None:
                user_id = result.group(1)

                meme_json = meme_dispatcher.getmemeuser(user_id)
                if meme_json is None:
                    return self.send_error(404)

                self.send_response(200)
                self.send_header('Content-type','application/json')
                self.end_headers()

                self.wfile.write(meme_json.encode("UTF-8"))

                return
            else:
                result = RE_GET_MEMEIMAGE.match(self.path)
                if result is not None:
                    meme_id = result.group(1)

                    url = meme_dispatcher.getmeme(meme_id)
                    if url is None:
                        return self.send_error(404)

                    self.send_response(200)
                    self.send_header('Content-type','image/png')
                    self.end_headers()

                    f = open(url, 'rb')
                    self.wfile.write(f.read())
                    f.close()

                    return
                else:
                    return self.send_error(400)
        except:
            logging.error('m3>Error processing GET request. \nPath: %s\nHeaders:\n%s\n', str(self.path), str(self.headers))
            return self.send_response(500)

            #logging.info("Requestline:\n%s\nSize (b): %i\n", str(self.requestline), sys.getsizeof(self.requestline))
            #logging.info("Requestline:\n%s\nSize (b): %i\n", str(self.requestline), len(bytes(str(self.requestline), "UTF-8")))
            #logging.info("Headers:\n%sSize (b): %i\n", str(self.headers), sys.getsizeof(self.headers))
            #logging.info("Headers:\n%sSize (b): %i\n", str(self.headers), len(bytes(str(self.headers), "UTF-8")))

        def do_PUT(self):
            try:
                result = RE_PUT_MEMELIKE.match(self.path)
                if result is None:
                    return self.send_error(400)
                else:
                    user_id = result.group(1)
                    meme_id = result.group(2)
                    likeable = result.group(3)

                    meme_dispatcher.putmemelike(user_id, meme_id, likeable)

                    self.send_response(200)
                    self.end_headers()
                    return
            except:
                logging.error('m3>Error processing PUT request. \nPath: %s\nHeaders:\n%s\n', str(self.path), str(self.headers))
                return self.send_response(500)

def run():
    print('m3>Starting HTTP server at ' + SERVER_ADDRESS + ':' + str(SERVER_PORT) + '...')
    logging.info('m3>Starting HTTP server at ' + SERVER_ADDRESS + ':' + str(SERVER_PORT) + '...')

    try:
        server_address = (SERVER_ADDRESS, SERVER_PORT)
        httpd = HTTPServer(server_address, Me3HTTPRequestHandler)

        print('m3>Running HTTP server at ' + SERVER_ADDRESS + ':' + str(SERVER_PORT) + '...')
        logging.error('m3>Running HTTP server at ' + SERVER_ADDRESS + ':' + str(SERVER_PORT) + '...')

        httpd.serve_forever()
    except:
        logging.error('m3>Error starting HTTP server at ' + SERVER_ADDRESS + ':' + str(SERVER_PORT) + '...')

if __name__ == '__main__':
    logging.basicConfig(filename='info.log', filemode='w', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',)
    run()

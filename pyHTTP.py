#!/usr/bin/python
# -*- coding: utf-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os

PORT_NUMBER = 8000

# MIME dictionary for file types
mime_dict = {'.html': 'text/html', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.js': 'application/javascript',
                '.css': 'text/css','.pdf': 'application/pdf', '.bmp': 'image/bmp', '.csv': 'text/csv', '.gif': 'image/gif',
                '.json': 'application/json', '.latex': 'application/x-latex', '.doc': 'application/msword',
                '.png': 'image/x-png', '.xml': 'application/rss+xml'}

class pyHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        root_dir    =  os.path.dirname(os.path.abspath(__file__)) # the directory of the python file
        if self.path == "/": # user doesn't specify the file path
            file_path           = root_dir + "/index.html" # search for the file index.html in the directory
        else:
            file_path           = root_dir + self.path
        # check if the file exists
        if os.path.isfile(file_path):
            self.send_response(200)
            _, file_extension   = os.path.splitext(file_path)
            if file_extension in mime_dict.keys():
                self.send_header('Content-type', mime_dict[file_extension])
            else:
                self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(file_path, 'rb') as f:
                self.wfile.write(f.read())
                f.close()
        else:
            self.send_error(404,'File Not Found: %s' % file_path)

def run():
    server      = HTTPServer(('', PORT_NUMBER), pyHTTP)
    print 'Serving HTTP server on port', PORT_NUMBER
    server.serve_forever()

if __name__ == "__main__":
    run()

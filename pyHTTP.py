#!/usr/bin/python
# -*- coding: utf-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
import urllib
import cgi
import sys
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

PORT_NUMBER = 8000

# MIME dictionary for file types
mime_dict = {'.html': 'text/html', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.js': 'application/javascript',
                '.css': 'text/css','.pdf': 'application/pdf', '.bmp': 'image/bmp', '.csv': 'text/csv', '.gif': 'image/gif',
                '.json': 'application/json', '.latex': 'application/x-latex', '.doc': 'application/msword',
                '.png': 'image/png', '.xml': 'application/rss+xml', '.py': 'text/x-python'}

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
            #if os.listdir(root_dir):
            if self.path == "/":
                # display all the files in the directory
                try:
                    file_list           = os.listdir(root_dir)
                except os.error:
                    self.send_error(404, "No permission to list directory")
                f = StringIO()
                f.write('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
                f.write("<html>\n<title>Directory listing for %s</title>\n" % self.path)
                f.write("<body>\n<h2>Directory listing for %s</h2>\n" % self.path)
                f.write("<hr>\n<ul>\n")
                for name in file_list:
                    fullname = os.path.join(root_dir, name)
                    displayname = linkname = name
                    # Append / for directories or @ for symbolic links
                    if os.path.isdir(fullname):
                        displayname = name + "/"
                        linkname = name + "/"
                    if os.path.islink(fullname):
                        displayname = name + "@"
                        # Note: a link to a directory displays with @ and links with /
                    f.write('<li><a href="%s">%s</a>\n' % (urllib.quote(linkname), cgi.escape(displayname)))
                f.write("</ul>\n<hr>\n</body>\n</html>\n")
                length = f.tell()
                f.seek(0)
                self.send_response(200)
                encoding = sys.getfilesystemencoding()
                self.send_header("Content-type", "text/html; charset=%s" % encoding)
                self.send_header("Content-Length", str(length))
                self.end_headers()
                self.wfile.write(f.getvalue())
            else:
                self.send_error(404,'File Not Found: %s' % file_path)



def run():
    server      = HTTPServer(('', PORT_NUMBER), pyHTTP)
    print 'Serving HTTP server on port', PORT_NUMBER
    server.serve_forever()

if __name__ == "__main__":
    run()

# pyHTTP
A simple implementation of a HTTP server in Python
## Introduction
By using the module BaseHTTPServer in Python 2.x, a server which serves the static files is implemented in Python. The server receives request file path from the client side (browser), and display the content of the file depending of the MIME type.
## MIME type
### What is a MIME type?
MIME stands for "Multipurpose Internet Mail Extensions. It's a way of identifying files on the Internet according to their nature and format. For example, using the "Content-type" header value defined in a HTTP response, the browser can open the file with the proper extension/plugin.
### What does a MIME type look like?
A MIME type is a string identifier composed of two parts: a "type" and a "subtype". The "type" refers to a logical grouping of many MIME types that are closely related to each other; it's no more than a high level category. "subtypes" are specific to one file type within the "type".

For example, the MIME value "application/xml" is used for XML documents and specifies that the "xml" subtype belongs in the "application" type.
### MIME tables
| Name | MIME type | File Extension |
| --- | --- | --- |
| Adobe Portable Document Format | application/pdf | .pdf |
| Bitmap Image File | image/bmp | .bmp |
| Comma-Seperated Values | text/csv | .csv |
| Graphics Interchange Format | image/gif | .gif |
| HyperText Markup Language (HTML) | text/html | .html |
| JavaScript | application/javascript | .js |
| JavaScript Object Notation (JSON) | application/json | .json |
| JPEG Image | image/jpeg | .jpg or .jpeg |
| LaTeX | application/x-latex | .latex |
| Microsoft Word | application/msword | .doc |
| RSS - Really Simple Syndication | application/rss+xml | .rss or .xml |
| Portable Network Graphics (PNG) | image/png | .png |
## How to run
Open a terminal in the same directory of the __pyHTTP.py__ file, and type
```
$python pyHTTP.py
Serving HTTP server on port 8000
```
Then open your browser and type http://localhost:8000, the server will display the file index.html if any in the directory, to access to other files, for example style.css, type http://localhost:8000/style.css. For the supported files type, refer to the MIME part.

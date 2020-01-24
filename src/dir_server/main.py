#!/usr/bin/python3

import http.server
import socketserver

PORT = 8070

handler = http.server.SimpleHTTPRequestHandler
handler.extensions_map.update({
    '.webapp': 'application/x-web-app-manifest+json',
});

httpd = socketserver.TCPServer(("", PORT), handler)

print("Serving at port", PORT)
httpd.serve_forever()

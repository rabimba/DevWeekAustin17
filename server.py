import BaseHTTPServer, SimpleHTTPServer
import ssl

# 0.0.0.0 allows connections from anywhere
httpd = BaseHTTPServer.HTTPServer(('0.0.0.0', 443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./cert.crt', keyfile='./key.key', server_side=True)
httpd.serve_forever()

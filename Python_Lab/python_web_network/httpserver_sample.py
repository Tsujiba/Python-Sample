"""
#############################################################################
httpserver：webサーバを立ち上げる（簡易的な）
#############################################################################

"""
import http.server
import socketserver

IP = '127.0.0.1'
PORT = 8000

with socketserver.TCPServer((IP, PORT), 
                            http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()

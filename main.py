from http.server import HTTPServer, BaseHTTPRequestHandler

class CustomHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write('Python HTTP webserver is up and running!'.encode())

def main():
    port = 8000
    server = HTTPServer(('',port), CustomHandler)
    print('Server started on port %s' %port)
    server.serve_forever()

if __name__ == '__main__':
    main()
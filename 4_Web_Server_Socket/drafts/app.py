from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import mimetypes
from pathlib import Path
import socket


def send_data_by_soket(data):
    host = socket.gethostname()
    port = 5000
    client_socket = socket.socket()
    client_socket.connect((host, port))
    client_socket.send(data)
    result = client_socket.recv(1024).decode()
    print(f'result: {result}')
    client_socket.close()


class HttpGetHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        data = self.rfile.read(int(self.headers.get('Content-Length')))
        data_string = data
        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()
        send_data_by_soket(data_string)

    def do_GET(self):
        url = urlparse(self.path)
        match url.path:
            case '/'|"/index.html":
                self.send_html('static/index.html') 
            case "/message.html":
                self.send_html('static/message.html')
            case _:
                file_path = Path(url.path[1:])
                if file_path.exists():
                    self.send_static(str(file_path))                
                else:
                    self.send_html('static/error.html', 404)
    
    def send_static(self, static_filename):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        self.send_header('Content-type', mt[0])
        self.end_headers()
        with open(static_filename, 'rb') as f:
            self.wfile.write(f.read())

    def send_html(self, html_filename, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(html_filename, 'rb') as f:
            self.wfile.write(f.read())

def run():
    server_class = HTTPServer
    handler_class = HttpGetHandler
    server_address = ('', 3000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == '__main__':
    run()
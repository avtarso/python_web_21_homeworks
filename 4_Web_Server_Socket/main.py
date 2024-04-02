from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, unquote_plus
from datetime import datetime
from pathlib import Path
import mimetypes
import socket
import json


from threading import Thread, Lock

SOCKET_PORT = 5000
HTTP_PORT = 3000
file_name = 'data/data.json'

lock = Lock()


def send_data_by_soket(data):
    host = socket.gethostname()
    client_socket = socket.socket()
    client_socket.connect((host, SOCKET_PORT))
    client_socket.send(data)
    result = client_socket.recv(1024).decode()
    print(result)
    client_socket.close()


def save_to_dict(file_name, data):
    data = unquote_plus(data)
    dict_data = {key: value for key, value in [el.split("=") for el in data.split("&")]}
    new_data_dict = {str(datetime.today()): dict_data}
    if Path(file_name).exists():
        with open(file_name, "r", encoding="utf-8") as fh:
            current_dict = json.load(fh)
        current_dict.update(new_data_dict)
        with open(file_name, "w", encoding="utf-8") as fh:
            json.dump(current_dict, fh, ensure_ascii=False, indent="\t")
    else:
        with open(file_name, "w", encoding="utf-8") as fh:
            json.dump(new_data_dict, fh, ensure_ascii=False, indent="\t")


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


def soket_server():
    host = socket.gethostname()
    server_socket = socket.socket()
    server_socket.bind((host, SOCKET_PORT))
    server_socket.listen()
    while True:
        conn, address = server_socket.accept()#
        data = conn.recv(1024).decode()
        if data:
            decoded_data = unquote_plus(data)
            save_to_dict(file_name, decoded_data)
            print(f'data received by socket server: {decoded_data}')

            message = "data saved in json file"
            conn.send(message.encode())


def run():
    server_class=HTTPServer
    handler_class=HttpGetHandler
    server_address = ('', HTTP_PORT)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == '__main__':
    t1 = Thread(target=soket_server)
    t2 = Thread(target=run)
    t1.start()
    t2.start()

import socket
from datetime import datetime
import json
from pathlib import Path
from _thread import *

file_name = 'data/data.json'


def save_to_dict(file_name, data):
    dict_data = {key: value for key, value in [el.split("=") for el in data.split("&")]}
    new_data_dict = {str(datetime.today()): dict_data}
    if Path(file_name).exists():
        with open(file_name, "r") as fh:
            current_dict = {}
            current_dict = json.load(fh)
        current_dict.update(new_data_dict)
        with open(file_name, "w") as fh:
            json.dump(current_dict, fh, indent="\t")
    else:
        with open(file_name, "w") as fh:
            json.dump(new_data_dict, fh, indent="\t")


def soket_server():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen()
    while True:
        conn, address = server_socket.accept()#
        data = conn.recv(1024).decode()
        if data:
            save_to_dict(file_name, data)
            print(f'data received by socket server: {data}')

            message = "data saved in json file"
            conn.send(message.encode())



if __name__ == '__main__':
    soket_server()
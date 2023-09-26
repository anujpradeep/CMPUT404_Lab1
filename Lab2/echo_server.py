import socket
from threading import Thread

BYTES_TO_READ = 4096
HOST = "localhost"
PORT = 8080

def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")

        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break

            print(data)
            conn.sendall(data)


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen()
        conn, addr = server_socket.accept()
        handle_connection(conn, addr)

#step 8
def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen()

        while True:
            conn, addr = server_socket.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()

if __name__ == "__main__":
    # start_server()
    start_threaded_server()
import socket
from threading import Thread

BYTES_TO_READ = 4096
HOST = "www.google.com"
PORT = 80
PROXY_HOST = "localhost"
PROXY_PORT = 8080

# This is the Proxy Client
def send_request(host, port, request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.send(request)
        client_socket.shutdown(socket.SHUT_WR)

        data = client_socket.recv(BYTES_TO_READ)
        result = b'' + data

        while (len(data) > 0):
            data = client_socket.recv(BYTES_TO_READ)
            result += data

        return result
    
# This is the Proxy Server
def handle_connection(conn, addr):
    with conn:
        print(f"Connected to {conn} by {addr}")

        request = b''
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print("data = {}",data)
            request += data
            
        response = send_request(HOST, PORT, request)

        conn.sendall(response)


#step 8
def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((PROXY_HOST, PROXY_PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen()

        while True:
            conn, addr = server_socket.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((PROXY_HOST, PROXY_PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen()

        conn, addr = server_socket.accept()
        handle_connection(conn, addr)

if __name__ == "__main__":
    # start_server()
    start_threaded_server()
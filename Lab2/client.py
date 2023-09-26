import socket

BYTES_TO_READ = 4096

#Talks to the proxy server which will make the request for us, and return the response back
HOST = ""
PORT = 8080


def get(host, port):
    request = b"GET / HTTP/1.1\nHost: " + host.encode('utf-8') + b"\n\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.send(request)
        
        client_socket.shutdown(socket.SHUT_WR)

        results = client_socket.recv(BYTES_TO_READ)

        while (len(results) > 0):
            print(results)
            results = client_socket.recv(BYTES_TO_READ)


if __name__ == "__main__":
    get(HOST, PORT)
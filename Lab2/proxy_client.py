import socket

BYTES_TO_READ = 4096

#As mentioned in lab, we don't really need this file, as proxy_server.py can handle the proxy client part

def get(host, port):
    request = b"GET / HTTP/1.1\nHost: www.google.com\n\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.send(request)
        client_socket.shutdown(socket.SHUT_WR)

        chunk = client_socket.recv(BYTES_TO_READ)
        result = b'' + chunk

        while (len(chunk) > 0):
            chunk = client_socket.recv(BYTES_TO_READ)
            result+= chunk
        return result
    
if __name__ == "__main__":
    host = "localhost"
    port = 8080
    get(host, port)
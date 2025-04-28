import socket


def reverse_string(s):
    return s[::-1]

def main():
    # host = '0.0.0.0'  # Listen on all interfaces
    host = '127.0.0.1'
    port = 7200

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        serverSocket.bind((host, port))
    except socket.error as e:
        print(f"Bind failed: {e}")
        return    
    serverSocket.listen(1)
    print(f"Server listening on port {port}...")
    conn, addr = serverSocket.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        print(f"Received from client: {data}")

        reversedString = reverse_string(data).encode()
        conn.send(reversedString)

        if data.lower() == "end":
            print("Received 'end' from client. Closing connection.")
            break

    conn.close()
    serverSocket.close()

if __name__ == "__main__":
    main()

import socket

def main():
    host = '127.0.0.1'
    port = 7200

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        clientSocket.connect((host, port))
    except Exception as e:
        print(f"Connection failed: {e}")
        return
    
    while True:
        message = input("Enter message (type 'end' to quit): ")
        clientSocket.send(message.encode())

        data = clientSocket.recv(1024).decode()
        print(f"Received from server: {data}")

        if message.lower() == "end" and data.lower() == "dne":
            print("Termination confirmed with 'dne'. Closing client.")
            break

    clientSocket.close()

if __name__ == "__main__":
    main()

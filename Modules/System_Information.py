import subprocess
import platform
import socket

def get_info():
    try:
        info = []

        # Basic info
        info.append(f"OS: {platform.system()} {platform.release()}")
        info.append(f"Version: {platform.version()}")
        info.append(f"Architecture: {platform.machine()}")

        # Network
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        info.append(f"Hostname: {hostname}")
        info.append(f"IP: {local_ip}")

        # User
        import os
        info.append(f"User: {os.getlogin()}")

        return "\n".join(info)
    except Exception as e:
        return f"Error gathering info: {e}"

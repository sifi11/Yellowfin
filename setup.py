import json
from cryptography.fernet import Fernet

# Initialize Fernet with your key
key = b'FtABmI-psWsyRuNo-ZqCGFjhdhUlB6RcNxORcdKcN7Q='
cipher = Fernet(key)

# Load existing data
with open('config.json', 'r') as file:
    data = json.load(file)

# Get new info
host = input("What's your server's IP? ")

# Encrypt each value and convert the resulting bytes to a string for JSON storage
data['host'] = cipher.encrypt(host.encode()).decode()

# Save as a standard readable JSON file
with open('config.json', 'w') as file:
    json.dump(data, file, indent=4)

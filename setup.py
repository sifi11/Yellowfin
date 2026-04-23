import json
from cryptography.fernet import Fernet

# Initialize Fernet with your key
key = b'FtABmI-psWsyRuNo-ZqCGFjhdhUlB6RcNxORcdKcN7Q='
cipher = Fernet(key)

# Load existing data
with open('config.json', 'r') as file:
    data = json.load(file)

# Get new info
a1 = input("What's your server's IP? ")
a2 = input("What's your server's port?(Put 4444) ")

# Encrypt each value and convert the resulting bytes to a string for JSON storage
data['a1'] = cipher.encrypt(host.encode()).decode()
data['a2'] = cipher.encrypt(port.encode()).decode()

# Save as a standard readable JSON file
with open('config.json', 'w') as file:
    json.dump(data, file, indent=4)

import os
from dotenv import load_dotenv
from pathlib import Path

print("=== URL Debug Test ===")

# Print current working directory and env file location
print(f"Working directory: {os.getcwd()}")
env_path = Path('.env')
print(f".env exists: {env_path.exists()}")

# Read the raw file content
print("\nRaw .env file contents:")
with open('.env', 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        print(f"Line {i+1}: '{line.strip()}'")
        # Check for any unusual characters
        print(f"Line {i+1} bytes:", [ord(c) for c in line])

print("\nTrying to load .env...")
load_dotenv(override=True)

# Check the specific variable
url = os.getenv('LIVEKIT_URL')
print("\nLIVEKIT_URL value check:")
print(f"Type: {type(url)}")
print(f"Value: {url}")
if url is not None:
    print(f"Length: {len(url)}")
    print(f"Characters:", [ord(c) for c in url])

# Try loading the variable directly from the file
print("\nTrying to parse URL directly from file:")
with open('.env', 'r') as f:
    for line in f:
        if line.startswith('LIVEKIT_URL='):
            print(f"Found URL line: '{line.strip()}'")
            url_value = line.split('=', 1)[1].strip()
            print(f"Extracted value: '{url_value}'")
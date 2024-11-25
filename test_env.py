import os
from dotenv import load_dotenv

print("Current directory:", os.getcwd())
print("\nBefore loading .env:")
print("LIVEKIT_URL =", os.getenv('LIVEKIT_URL'))

print("\nLoading .env file...")
load_dotenv(verbose=True)

print("\nAfter loading .env:")
print("LIVEKIT_URL =", os.getenv('LIVEKIT_URL'))
print("LIVEKIT_API_SECRET =", os.getenv('LIVEKIT_API_SECRET'))
print("LIVEKIT_API_KEY =", os.getenv('LIVEKIT_API_KEY'))
print("OPENAI_API_KEY =", os.getenv('OPENAI_API_KEY'))

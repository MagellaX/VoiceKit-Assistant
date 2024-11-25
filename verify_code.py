import os

def read_file_content():
    print("=== Code Verification ===")
    
    file_path = 'main.py'
    print(f"File exists: {os.path.exists(file_path)}")
    
    print("\nCurrent content of main.py:")
    with open(file_path, 'r') as f:
        content = f.read()
        print(content)
    
    print("\nFile size:", os.path.getsize(file_path), "bytes")
    print("Last modified:", os.path.getmtime(file_path))

read_file_content()
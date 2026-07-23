# File operations with clear messages
import os
print(f"1. Current directory: {os.getcwd()}")
print(f"2. Files here: {os.listdir('.')[:5]}")  # First 5 files
print(f"3. Windows version: {os.environ.get('COMPUTERNAME', 'Unknown')}")


# Subprocess with visible output
import subprocess
result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
print("=== DIR Command Output ===")
print(result.stdout[:500])  # Show first 500 characters
print("=== End of Output ===")

# Multiple commands in one script
import os, subprocess, socket

print("=" * 50)
print("WINDOWS SYSTEM INFO")
print("=" * 50)

# Current directory
print(f"\n[1] Current Path: {os.getcwd()}")

# Computer name
print(f"[2] Computer Name: {os.environ['COMPUTERNAME']}")

# Username
print(f"[3] Current User: {os.environ['USERNAME']}")

# IP address
try:
    ip = socket.gethostbyname(socket.gethostname())
    print(f"[4] IP Address: {ip}")
except:
    print(f"[4] IP Address: Unable to get")

# Ping test
result = subprocess.run(["ping", "-n", "1", "127.0.0.1"], capture_output=True)
print(f"[5] Local Network: {'Working' if result.returncode == 0 else 'Failed'}")

print("\n" + "=" * 50)
print("Script completed!")


# Print all environment variables
#for key, value in os.environ.items():
#    print(f"{key} = {value}")

#print (f"Test socket:{socket.getaddrinfo(socket.gethostname(),80)}")
#print (f"FQDN:{socket.getfqdn()}")

# test.py - copy entire block and run
import os, sys, platform, psutil, subprocess, socket
print("="*50)
print(f"Windows: {platform.version()}")
print(f"Computer: {os.environ['COMPUTERNAME']}")
print(f"User: {os.environ['USERNAME']}")
print(f"CPU: {psutil.cpu_percent()}%")
print(f"RAM: {psutil.virtual_memory().percent}%")
print(f"Disk C: {psutil.disk_usage('C:').percent}% used")
print(f"IP: {socket.gethostbyname(socket.gethostname())}")
print("="*50)
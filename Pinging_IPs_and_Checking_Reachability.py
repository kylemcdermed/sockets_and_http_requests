import socket
import subprocess
import time
import requests

ip_list = ['www.kitco.com','www.bloomberg.com','www.gemini.com','www.nyse.com']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for site in ip_list:
    
    ip = socket.gethostbyname(site)
    print(f'IP for {site}: {ip}')
    
    start_time = time.time()
    res = subprocess.Popen(['ping','-n','1',ip],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout,stderr = res.communicate()
    end_time = time.time()

    if res.returncode == 0:
        elapsed_time = start_time - end_time
        print(f'The site {site} had a response time of {elapsed_time:.4f} seconds')
    else:
        print(f'Failed to reach site {site} (IP: {ip})')
    

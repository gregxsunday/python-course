import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.settimeout(1)
address = ('8.8.8.8', 443)
mysocket.connect_ex(address)
mysocket.close()
import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.settimeout(1)

address = ('8.8.8.8', 443)
result = mysocket.connect_ex(address)

if result == 0:
    print(f'port jest otwarty')

mysocket.close()
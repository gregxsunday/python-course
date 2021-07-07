import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.settimeout(1)
ip = '8.8.8.8'
port = 443
address = (ip, port)
result = mysocket.connect_ex(address)

if result == 0:
    print('port', port, 'jest otwarty')

mysocket.close()


mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.settimeout(1)

ip = '8.8.8.8'
port = 80
address = (ip, port)

result = mysocket.connect_ex(address)

if result == 0:
    print('port', port, 'jest otwarty')



mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.settimeout(1)

ip = '8.8.8.8'
port = 53
address = (ip, port)

result = mysocket.connect_ex(address)

if result == 0:
    print('port', port, 'jest otwarty')

mysocket.close()
import socket

def is_port_open(port, ip='8.8.8.8'):
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.settimeout(1)

    address = (ip, port)

    result = mysocket.connect_ex(address)
    mysocket.close()

    if result == 0:
        return True
    else:
        return False



for port in range(52, 1024):
    # if is_port_open(port, '1.1.1.1'):
    if is_port_open(port):
        print('port', port, 'jest otwarty', end='\n\n\n\n')
    else:
        print('port', port, 'jest zamknięty', sep='|')

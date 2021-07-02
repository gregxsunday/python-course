import socket

if __name__ == '__main__':

    ports = [80, 53, 443, 3306]

    for port in ports:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.settimeout(1)
        result = mysocket.connect_ex(('8.8.8.8', port))

        if result == 0:
            print(f'port {port} open')
        mysocket.close()
import socket

def is_port_open(port, ip):
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.settimeout(1)

    address = (ip, port)

    result = mysocket.connect_ex(address)
    mysocket.close()

    if result == 0:
        return True
    else:
        return False


# server = {
#     1: 'closed',
#     2: 'closed',
#     3: 'open'
# }


# server = {
#     53: {
#         'status': 'closed', 
#         'service': None
#         },
#     80: {
#         'status': 'closed', 
#         'service': None
#         },
#     443: {
#         'status': 'open', 
#         'service': 'Apache'
#         },
# }

server = {}

for port in [53, 80, 443]:
    if is_port_open(port, '8.8.8.8'):
        server[port] = 'open'
        # print('port', port, 'jest otwarty')
    else:
        server[port] = 'closed'
        # print('port', port, 'jest zamknięty')

print('# Porty w słowniku')
for port in server:
    print(port)

print('\n# Porty w słowniku używając .keys()')
for port in server.keys():
    print(port)

print('\n# Statusy w słowniku używając .values()')
for status in server.values():
    print(status)

print('\n# Porty i statusy w słowniku używając .items()')
for port, status in server.items():
    print(port, status)
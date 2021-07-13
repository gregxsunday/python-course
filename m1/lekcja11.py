import socket

class Port:
    def __init__(self, ip, port_number):
        self.ip = ip
        self.port_number = port_number


    def check_port(self):
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.settimeout(1)

        address = (self.ip, self.port_number)

        result = mysocket.connect_ex(address)
        mysocket.close()

        if result == 0:
            self.open = True
        else:
            self.open = False
    
    def print_status(self):
        if self.open:
            print(self.port_number, 'open')
        else:
            print(self.port_number, 'closed')

    def __str__(self):
        if self.open:
            return str(self.port_number) + ' open'
        else:
            return str(self.port_number) + ' closed'
        



# server = {
#     1: {
#         'status': 'closed', 
#         'service': None
#         },
#     2: {
#         'status': 'closed', 
#         'service': None
#         },
#     3: {
#         'status': 'open', 
#         'service': 'Apache'
#         },
# }

ip = '8.8.8.8'
ports = []
for port_number in [53, 80, 443]:
    port = Port(ip, port_number)
    port.check_port()
    ports.append(port)

for port in ports:
    # port.print_status()
    print(port)
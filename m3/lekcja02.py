import requests

if __name__ == '__main__':
    sess = requests.Session()
    proxies = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080'
    }
    sess.proxies = proxies
    sess.verify = False

    login, password = 'user', 'pass'

    data = {
        'login': login,
        'password': password
    }
    # sess.get('http://127.0.0.1/profile')

    sess.post('http://127.0.0.1/login', data=data)

    # sess.get('http://127.0.0.1/profile')

    # sess.cookies.set("mycookie", "myvalue", domain="127.0.0.1")

    # sess.get('http://127.0.0.1/profile')

    headers = {
        'Authorization': 'Bearer eyJ...',
        'X-Naglowek': 'Wartosc'
    }
    # sess.get('http://127.0.0.1/profile', headers=headers)

    sess.headers = headers
    sess.get('http://127.0.0.1/profile')



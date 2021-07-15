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

    sess.post('http://127.0.0.1/login', data=data)


    headers = {
        'Authorization': 'Bearer eyJ...'
    }
    sess.get('http://127.0.0.1/profile', headers=headers)

    sess.headers = headers
    sess.get('http://127.0.0.1/profile')



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

    resp = sess.post('http://127.0.0.1/login', data=data)

    data = {
        'name': 'nazwa',
        'content': 'zawartosc'
    }

    # resp = sess.post('http://127.0.0.1/notes/', data=data)
    print(f'{resp.status_code=}')
    print(f'{sess.cookies.get_dict()=}')
    print(f'{resp.headers=}')
    # print(f'{resp.text=}')
    # print(f'{resp.content=}')
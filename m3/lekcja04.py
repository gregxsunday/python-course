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

    resp = sess.post('http://127.0.0.1/login', data=data, allow_redirects=False)

    # print(f'{resp.status_code=}')
    # print(f'{resp.next.url=}')




    if resp.next.url == 'http://127.0.0.1/login':
        print('błąd logowania')
    elif resp.next.url == 'http://127.0.0.1/profile':
        print('logowanie udane')
        print(f'{resp.next=}')
        sess.send(resp.next)
        # print(f'{resp.headers=}')
        # print(f'{sess.cookies.get_dict()=}')
        # print(f'{resp.json()=}')
        print(f'{type(resp.text)=}')
        print(f'{type(resp.content)=}')
    else:
        print('niespodziewany błąd')
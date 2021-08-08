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

    data = {
        'name': 'nazwa',
        'content': 'zawartosc'
    }

    # sess.post('http://127.0.0.1/notes/', data=data)

    # sess.put('http://127.0.0.1/notes/', json=data)


    # with open('lekcja03.py', 'r') as infile:
    #     files = {
    #         'myfile': infile.read()
    #     }
    #     sess.post('http://127.0.0.1/notes/', files=files)

    with open('lekcja03.py', 'r') as infile:
        files = {
            'myfile': ('filename.txt', infile.read(), 'text/html')
        }
        sess.post('http://127.0.0.1/notes/', files=files)
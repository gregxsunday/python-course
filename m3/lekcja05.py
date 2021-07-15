import requests
from bs4 import BeautifulSoup


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
    print(resp.text)

    # resp = sess.get('http://127.0.0.1/login')
    # soup = BeautifulSoup(resp.text, features="html.parser")
    # print(soup.find_all("input"))
    # print(soup.find_all(attrs={'class': 'button'}))
    # csrf_token_tag = soup.find("input", attrs={'name': 'csrf_token'})
    # print(csrf_token_tag)
    # print(csrf_token_tag['value'])
    # csrf_token = csrf_token_tag['value']

    # data['csrf_token'] = csrf_token

    # resp = sess.post('http://127.0.0.1/login', data=data)
    # print(resp.url)
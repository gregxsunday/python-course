from hashlib import sha256

if __name__ == '__main__':
    data = 'xss'

    # print(sha256(data))
    # print(sha256(data.encode('utf8')))
    # print(sha256(data.encode()))
    # print(sha256(data.encode()).hexdigest())

    # print(sha256('xss').hexdigest())
    # print(sha256('xss'.encode()).hexdigest())
    print(sha256(b'xss').hexdigest())
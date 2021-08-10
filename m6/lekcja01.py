import jwt

if __name__ == '__main__':
    headers = {
        "typ" : "JWT",
        "alg" : "HS256"
        }
    payload = {
        "user": "admin"
        }
    key = 'haslomaslo'

    token = jwt.encode(payload=payload, headers=headers, key=key)
    print(token)

    decoded = jwt.decode(token, key=key, algorithms=['HS256'])
    print(f'{decoded=}')
    # decoded = jwt.decode(token, key='', algorithms=['HS256'], options={'verify_signature': False})
    # print(f'{decoded=}')

    keys = ['qwerty', '123456', 'haslo', 'maslo', 'haslomaslo', 'asdfgh']

    for key in keys:
        new_token = jwt.encode(payload=payload, headers=headers, key=key)
        if new_token == token:
            print('found valid key:', key)
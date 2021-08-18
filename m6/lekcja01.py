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
    # print(token)

    # decoded = jwt.decode(token, key=key, algorithms=['HS256'])
    # print(f'{decoded=}')
    # decoded = jwt.decode(token, key='', algorithms=['HS256'], options={'verify_signature': True})
    # print(f'{decoded=}')

    keys = ['qwerty', '123456', 'haslo', 'maslo', 'haslomaslo', 'asdfgh']


    for key in keys:
        try:
            decoded = jwt.decode('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.rDMVRRkhG_d9fv_OJZf_G3nrLngVjcaROzRBLM0iwbI', key=key, algorithms=['HS256'])
            print('found valid key:', key)
        except jwt.exceptions.InvalidSignatureError:
            pass

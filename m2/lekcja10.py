if __name__ == '__main__':
    security = {
        'vulns' : ['xss', 'rce', 'lfi']
    }
    # print(security['vulnerabilities'])

    # try:
    #     # print(security['vulnerabilities'])
    #     print(security['vulns'][4])
    # except KeyError:
    #     print('no such key')


    # try:
    #     print(security['vulns'][4])
    # except (KeyError, IndexError):
    #     print('no such key')


    
    try:
        f = open('ffuf.log')
        print(security['vulns'][4])
    except KeyError:
        print('no such key')
    except IndexError as e:
        print('IndexError:', e)
    finally:
        print('finally')
        f.close()

import re

if __name__ == '__main__':
    with open('ffuf.log', 'r') as infile:
        logs = infile.read()

    for log in logs.split('\n'):
        log = log.replace(', ', ' ')
        log_split = log.split(' ')

        path = log_split[0]
        status_code = log_split[2]

        js = path.find('.js')
        
        # if js != -1 and status_code == '200':
        #     print(f'{path=}')
        
        # js = re.search('.js', path)
        # if js:
        #     print(path)

    # try:
        # result = re.search('.js', 'xjs').group()
        # result = re.search('\.js', '.js').group()
        # result = re.search('^js', 'jsx').group()
        # result = re.search('js$', 'jsx').group()
        # result = re.search('a', 'aaaaaa').group()
        # result = re.search('a?', 'aaaaaa').group()
        # result = re.search('a?', '').group()
        # result = re.search('a*', '').group()
        # result = re.search('a*', 'aaaaaaaa').group()
        # result = re.search('a+', 'aaaaa').group()
        # result = re.search('a+', '').group()
        # result = re.search('a{3}', 'asa').group()
        # result = re.search('a{2,4}', 'aaaaa').group()
        # result = re.search('a{2,4}', 'a').group()
        # result = re.search('[abc]{3}', 'bbb').group()
        # result = re.search('[abcp]{3}', 'bcpa').group()
        # result = re.search('[a-z]{3}', 'ab1cb2deFghi').group()
        # result = re.search('[a-zA-Z0-9\.\"]{3}', 'ab"1cb2d.eFghi').group()
    #     print(result)
    # except AttributeError:
    #     print('no match')
        

        js = re.search('\.js$', path)
        if js:
            print(path)
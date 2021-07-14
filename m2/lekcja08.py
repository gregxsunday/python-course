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
        
        if js != -1 and status_code == '200':
            print(f'{path=}')
        
        # js = re.search('.js', path)
        # if js:
        #     print(path)

        ### ipython
        

        # js = re.search('\.js$', path)
        # if js:
        #     print(path)
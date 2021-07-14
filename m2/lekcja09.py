import re
from termcolor import colored


if __name__ == '__main__':
    with open('ffuf.log', 'r') as infile:
        logs = infile.read()

    for log in logs.split('\n'):
        log = log.replace(', ', ' ')
        log_split = log.split(' ')

        path = log_split[0]
        status_code = log_split[2]
        size = log_split[4]        

        js = re.search('\.js$', path)
        if js:
            with open('js.txt', 'a') as outfile:
                # print(path, status_code, size)
                # print(path, status_code, size, file=outfile)
                # print(f'{path}|{status_code}|{size}', file=outfile)
                # print(path, status_code, size, file=outfile, sep='|')
                print(path, status_code, size, file=outfile, sep='|', end=';\n')
                print(colored(path, 'red'), colored(status_code, 'green'), colored(size, 'blue'), sep='|', end=';\n')
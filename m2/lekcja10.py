import re

if __name__ == '__main__':
    with open('ffuf.log', 'r') as infile:
        logs = infile.read()

    logs = [log.replace(', ', ' ').split(' ') for log in logs.split('\n')]
    logs = list(filter(lambda log: re.search('\.js$', log[0]), logs))
    [print(log[0]) for log in logs]
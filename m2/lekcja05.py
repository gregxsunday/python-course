if __name__ == '__main__':
    with open('ffuf.log', 'r') as infile:
        logs = infile.read()

    # print(logs.split('\n'))

    for log in logs.split('\n'):
        # print(f'linia: {log}')
        log_split = log.split(' ')
        # print(log_split)
        path = log_split[0]
        status_code = log_split[2]
        size = log_split[4]
        print(f'{path}|{status_code}|{size}')

        print('|'.join([path, status_code, size]))

if __name__ == '__main__':
    with open('ffuf.log', 'r') as infile:
        logs = infile.read()

    for log in logs.split('\n'):
        log_split = log.split(' ')
        path = log_split[0]
        status_code = log_split[2]
        size = log_split[4]
        # print(f'path: {path} | status code: {status_code} | size: {size}')

        # print(log)
        # print('|'.join(log_split))

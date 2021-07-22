if __name__ == '__main__':
    with open('ffuf.log', 'r') as infile:
        logs = infile.read()

    log = logs.split('\n')[0]
    # print(f'{log=}')

    log_split = log.split(' ')
    print(f'{log_split=}')
    # print(f'{log_split[0]=}')
    # print(f'{log_split[2:4]=}')
    # print(f'{log_split[:4]=}')
    # print(f'{log_split[2:-2]=}')
    # print(f'{log_split[:-1]=}')
    # print(f'{log_split[:]=}')
    # print(f'{log_split[-5:]=}')
    print(f'{log_split[::2]=}')


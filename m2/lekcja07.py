if __name__ == '__main__':
    with open('ffuf.log', 'r') as infile:
        logs = infile.read()

    for log in logs.split('\n'):
        # log_split = log.split(' ')
        # print(f'{log_split=}')
        log = log.replace(', ', ' ')
        log_split = log.split(' ')
        # print(f'{log_split=}')

        path = log_split[0]
        status_code = log_split[2]

        wp_admin = path.find('wp-admin')

        # if wp_admin != -1 and status_code == "200":
        #     print(f'{path=}\twp-admin found at index: {wp_admin}')
        # else:
        #     print(f'{path=}\twp-admin not found. {wp_admin=}')

        js = path.find('.js')
        
        # if wp_admin != -1 and js == -1 and status_code == '200':
        #     print(f'{path=}')


        if wp_admin != -1 and '.js' not in path and status_code == '200':
            print(f'{path=}')
        
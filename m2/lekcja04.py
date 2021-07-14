if __name__ == '__main__':
    infile = open('ffuf.log', 'r')
    logs = infile.read()
    print(logs)
    infile.close()

    # with open('ffuf.log', 'r') as infile:
    #     logs = infile.read()
    #     print(logs)

    # with open('ffuf.log', 'r') as infile:
    #     logs = infile.write('zapis')

    # with open('test.txt', 'w') as outfile:
    #     logs = outfile.write('zapis')

    # with open('test.txt', 'w') as outfile:
    #     print('zapis', file=outfile)

    # with open('test.txt', 'w') as outfile:
    #     print('dopisanie', file=outfile)

    # with open('test.txt', 'a') as outfile:
    #     print('dopisanie', file=outfile)

    
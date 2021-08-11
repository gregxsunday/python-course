from sys import argv
import argparse

if __name__ == '__main__':
    # print(f'{argv=}')
    # ip = argv[1]
    # port_start = argv[2]
    # port_end = argv[3]

    parser = argparse.ArgumentParser(description='Mój skaner portów. Użyj go, żeby sprawdzić jakie porty są otwarte na Twoim serwerze.')
    # parser.add_argument('-i', '--ip')
    # parser.add_argument('-i', '--ip', required=True)
    # parser.add_argument('-i', '--ip', required=True, help='Adres IP do przeskanowania')
    parser.add_argument('-i', '--ip', nargs=1, type=str, required=True, help='Adres IP do przeskanowania')
    # parser.add_argument('-p', '--ports', nargs=2)
    # parser.add_argument('-p', '--ports', nargs=2, default=[0, 65535])
    parser.add_argument('-p', '--ports', nargs=2, default=[0, 65535], metavar=('START', 'END'), help='Porty do przeskanowania')
    args = parser.parse_args()
    print(args)

    # print(f'Adres IP: {args.ip}')``
    print(f'Adres IP: {args.ip[0]}')
    # print(f'Porty: {args.ports}')
    print(f'Porty: {args.ports[0]}-{args.ports[1]}')


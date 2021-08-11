import os
import subprocess

if __name__ == '__main__':
    filename = input('Podaj nazwę pliku: ')
    # os.system(f'cat {filename}')

    # result = subprocess.run(['cat', filename], capture_output=True)
    result = subprocess.run(['cat', filename], capture_output=True, text=True)
    # print(end='\n\n\n')
    # print(result)
    print(type(result.stdout))
    print(result.stdout)
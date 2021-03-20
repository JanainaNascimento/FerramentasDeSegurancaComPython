import os
import time

with open('ping multiplo/host.txt') as file:#passa o caminho onde o arquivo esta
    dump = file.read()#le o arquivo
    dump = dump.splitlines()#organiza as linhas do arquivo

    qtdpacotes = input('Digite a quantidade de pacotes: ')

    for ip in dump:
        print('Verificandondo os IPs: ')
        os.system(f'ping -n {qtdpacotes} {ip}')
        time.sleep(1)

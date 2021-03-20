import os

ip_ou_host = input('Digite o IP ou host para ser verifcado: ')
qtdpacostes = input('Digite a quantidade de pacotes: ')

os.system(f'ping -n {qtdpacostes} {ip_ou_host}')

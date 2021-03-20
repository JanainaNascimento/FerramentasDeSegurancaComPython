
import socket

ip = input('Digite o IP: ')

for porta in range(1, 65535):
    s = socket.socket()
    s.settimeout(0.01)

    if s.connect_ex((ip, porta)) == 0:
        print(f'Porta: {porta} [ABERTA]')
        s.close()

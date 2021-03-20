import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as errosocket:   
        print('A conexão falhou!!!')
        print(f'Erro: {errosocket}')
        sys.exit()
    
    print('Socket criado com sucesso!')

    HostAlvo = input('Digite o Host ou o IP para conectar: ')
    PortaAlvo = input('Digite a porta a ser conectada: ')

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print(f'cliente tcp conectado com sucesso! \nNo host: {HostAlvo}\nNa porta: {PortaAlvo}')
        s.shutdown(2)

    except socket.error as errocliente:
        print(f'Não foi possivel conectar! \nNo host: {HostAlvo}\nNa porta: {PortaAlvo}')
        print(f'Erro: {errocliente}')
        sys.exit()

if __name__ == "__main__":
    main()

import hashlib
while True:
    string = input('Digite o texto a ser gerado o hash: ')

    menu = int(input('''### MENU - ESCOLHA O TIPO DE HASH ###
                    1) MD5
                    2) SHA1
                    2) SHA256
                    4) SHA512
    Digite o número do hash a ser gerado: '''))


    if menu == 1:
        resultado = hashlib.md5(string.encode('utf-8'))
        print(f'O hash de MD5 para a string "{string}" é:', resultado.hexdigest())
        break

    elif menu == 2: 
        resultado = hashlib.sha1(string.encode('utf-8'))
        print(f'O hash de SHA1 para a string "{string}" é:', resultado.hexdigest())
        break

    elif menu == 3:
        resultado = hashlib.sha256(string.encode('utf-8'))
        print(f'O hash de SHA256 para a string "{string}" é:', resultado.hexdigest())
        break

    elif menu == 4:
        resultado = hashlib.sha512(string.encode('utf-8'))
        print(f'O hash de SHA512 para a string "{string}" é:', resultado.hexdigest())
        break
    
    else:
        print('Algo deu errado tente novamente! Digite apenas uma das opções!')

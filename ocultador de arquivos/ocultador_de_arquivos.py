import ctypes

# pasta = input('Digite o caminho do arquivo a ser ocultado: ')

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_ocultar)

if retorno:
    print('Arquivo ocultado!')
else:
    print('O arquivo não foi ocultado')
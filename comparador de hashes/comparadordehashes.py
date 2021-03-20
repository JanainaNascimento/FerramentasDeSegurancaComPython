import hashlib

arquivo1 =  'comparador de hashes/a.txt'
arquivo2 = 'comparador de hashes/b.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo: a.txt é diferente do arquivo: b.txt')
    print(f'O hash do arquivo a.txt: {hash1.hexdigest()}')
    print(f'O hash do arquivo b.txt: {hash2.hexdigest()}')
else:
    print(f'O arquivo: a.txt é igual ao arquivo: b.txt')
    print(f'O hash do arquivo a.txt: {hash1.hexdigest()}')
    print(f'O hash do arquivo b.txt: {hash2.hexdigest()}')

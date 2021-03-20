import random, string

tamanho = int(input('Digite o tamanho de senha que voce deseja: ')) #tamanho da senha

chars = string.ascii_letters + string.digits + 'ç!@#$%¨&*()_-=.,/\|}{[]~^><:;?"+'
rnd = random.SystemRandom()

#pega cada caracter randomico gerado atraves do chars para cada i no range tamanho vai gerar um novo símbolo caracter
print(f''.join(rnd.choice(chars) for i in range(tamanho)))

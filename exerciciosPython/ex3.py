nome_esperado = 'Gabriel'
senha_esperada = 1308

nome = input('Digite seu primeiro nome: ')
senha = int(input("Digite uma senha de 4 números: "))

if nome == nome_esperado and senha == senha_esperada:
    print('Nome e senha cadastrados com sucesso!')
else:
    print('Erro. Tente novamente')
#senha incorreta

senha = str(input('Digite a senha: '))

while senha != 'python123':
    print('Senha incorreta! Digite novamente :')
    senha = input('Digite a senha: ')

print('Acesso liberado! ')
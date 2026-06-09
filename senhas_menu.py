#sistema de acesso + menu_simples 

print('Olá ! ')
nome = input('Qual o seu nome ? ')
senha = input('Por favor, digite sua senha : ')

tentativas = 1
max_tentativas = 3


while senha != 'python123':
    if tentativas >= max_tentativas:
        print('Número maximo atingido, encerrando programa')
        exit()
    print(f'Senha incorreta! Tentativa {tentativas} de {max_tentativas} :')
    senha = input('Por favor, digite sua senha : ')
    tentativas += 1
        

print (f'Bem vindo {nome}!')


while True:
    num  = int(input('Digite um dos numeros para: \n 1 - Mostrar mensagem \n 2 - Mostrar outra mensagem \n 0 - Sair \n '))

    if num == 1:
        print('O dia esta bonito! ')
    elif num == 2:
        print('As gramas estão verdes ')
    elif num == 0: 
        print('Adeus ! ')
        break
    else:
        print('Digite um numero valido') 
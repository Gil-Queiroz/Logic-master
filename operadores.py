#classificador de notas 
nota = int(input("Digite sua nota : "))
if nota > 10: 
    print("A prova vale 10 pontos, digite sua nota corretamente. ")
else:
    if nota <= 4:
        print("Você foi reprovado! ")
    elif nota >= 5 and nota <=6:
        print("Você está de recuperação")
    else : 
        print("Você foi aprovado! " )



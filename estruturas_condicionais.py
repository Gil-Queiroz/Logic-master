#calculadora básica 
num1 = float(input("Digite um numero : "))
num2 = float(input("Digite mais um numero : "))

soma = num1 + num2 
sub = num1 - num2
mult = num1 * num2

if num2 == 0:
    div = ("Não é possivel dividir por 0 ")
else: 
    div = num1 / num2

print(f"Resultado: \n A soma dos valores = {soma}  \n A subtração dos valores = {sub} \n A multiplicação dos valores = {mult} \n A divisão dos valores = {div} ")

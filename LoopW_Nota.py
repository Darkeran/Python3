''' Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o 
valor seja inválido e continue pedindo até que o usuário informe um valor válido. '''

loop = 1
while loop > 0:
    nota = int(input("Diga uma nota de 1 a 10:", ))
    if nota > 0 and nota < 11:
        print("Valor Valido")
        break
    else:
        print("Valor Invalido")

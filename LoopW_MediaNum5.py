''' Faça um programa que leia 5 números e informe a soma e a média dos números. '''

soma_num = 0
numero = 0
while numero < 5:
    num = int(input("Digite um número: ",))
    soma_num = num + soma_num
    numero = numero + 1

media_num = soma_num / 5
print("A soma dos números é:",soma_num)
print("A media dos números é:",media_num)

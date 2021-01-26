''' Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares. '''

Lista_Impar = []
Lista_Par = []
loop = 0
while loop < 10:
    Numero = int(input("Digite um número inteiro: ",))
    loop = loop + 1
    if Numero % 2 == 0:
        Lista_Par.append(Numero)
    elif Numero % 2 == 1:
        Lista_Impar.append(Numero)
print("Impar", len(Lista_Impar))
print("Par", len(Lista_Par))

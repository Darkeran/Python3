# Faça um programa que leia 5 números e informe o maior número

lista = []
Numero = 0
while Numero < 6:
    Maior_Num = int(input("Digite um número: ",))
    lista.append(Maior_Num)
    lista.sort(reverse=True)
    Numero = Numero + 1
print(lista[0])

# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo

lista = []
Fibonacci_1 = 1
Fibonacci_2 = 1

numero = int(input("Digite um número: ",))
while numero > Fibonacci_2:
    lista.append(Fibonacci_2)
    Fibonacci_2 = Fibonacci_1 + Fibonacci_2
    if Fibonacci_1 > numero:
        break
    lista.append(Fibonacci_1)
    Fibonacci_1 = Fibonacci_2 + Fibonacci_1
print(lista)
    

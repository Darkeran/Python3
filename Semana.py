Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.


semana = ["Número invalido","Domingo","Segunda-Feira","Terca-Feira","Quarta-Feira","Quinta-Feira","Sexta-Feira","Sabádo"]
numero = int(input("Insira um número que corresponda ao dia da semana:", ))

if numero < 0 or numero > 7: 
    print("Número invalido")

else:  
    print(semana[numero])

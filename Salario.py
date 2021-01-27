# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 


horas = float(input("Quantas horas você trabalha por mês: " ))
salario = float(input("E quantos que você recebe por hora: " ))
total = float(horas * salario)
print("Você recebe {} por hora trabalhada e nesse mês você trabalhou {} horas, então o seu salário deste mês vai ser de {}".format(salario, horas, total))

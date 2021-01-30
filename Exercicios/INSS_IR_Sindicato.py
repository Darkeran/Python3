# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:                                            
# - salário bruto.
# - quanto pagou ao INSS.
# - quanto pagou ao sindicato.
# - o salário líquido.                                                                                          

horas_trabalhadas = float ( input("Quantas horas você trabalhou neste mês:", ))
ganho_hora = float  (input("Quantos que você recebo por hora:", ))

salario_bruto = ganho_hora * horas_trabalhadas
desconto_inss = (salario_bruto * 8) / 100
desconto_ir = (salario_bruto * 11) / 100
desconto_sindicato = (salario_bruto * 5) / 100
salario_liquido = salario_bruto - desconto_sindicato - desconto_ir - desconto_inss

print("Seu sálario bruto neste mês é de R$%.2f" %salario_bruto)
print("Total descontado do INSS R$%.2f" %desconto_inss)
print("Total descontado do IR R$%.2f" %desconto_ir)
print("Total descontado do sindicato R$%.2f" %desconto_sindicato)
print("Seu sálario liquido neste mês é de R$%.2f" %salario_liquido)


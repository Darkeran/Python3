''' As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    - salários até R$ 280,00 (incluindo) : aumento de 20%
    - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    - salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    - salário antes do reajuste;
    - percentual de aumento aplicado;
    - valor do aumento;
    - novo salário, após o aumento.                                                                                                                         '''
                                                                                                                                                       
salario_inicial = float(input("Qual é o seu salário em R$: ",))
porcentagem = 0

if salario_inicial <= 280.00:

    salario_depois = ((salario_inicial * 20 ) / 100) + salario_inicial
    porcentagem = 20

elif salario_inicial > 280.00 and salario_inicial <= 700.00:

    salario_depois = ((salario_inicial * 15) / 100) + salario_inicial
    porcentagem = 15

elif salario_inicial > 700.00 and salario_inicial <= 1500.00:

    salario_depois = ((salario_inicial * 10) / 100) + salario_inicial
    porcentagem = 10

else:

    salario_depois = ((salario_inicial * 5) / 100) + salario_inicial
    porcentagem = 5

print ("O seu salário antes do reajuste era de R$%.2f" %(salario_inicial))
print (("O percentual do reajuste foi de {}%").format(porcentagem))
print ("O valor total do seu aumento foi de R$%.2f" %((salario_inicial * porcentagem) / 100))
print ("O seu salário ápos o aumento é de R$%.2f" %(salario_depois))

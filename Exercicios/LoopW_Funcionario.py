# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro 
# do percentual do ano anterior. Faça um programa que determine o salário atual desse 
# funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o 
# salário inicial do funcionário. 



Percentual = 1.5
Salario_Inicial = 1000
Aumento = ( Percentual * Salario_Inicial) / 100
Salario_Final = Salario_Inicial + Aumento
Ano = 1995
while Ano <= 2021:
    Percentual = Percentual * 2
    Aumento = ( Percentual * Salario_Final) / 100
    Salario_Final = Salario_Final + Aumento
    Ano = Ano + 1
print("Salário Inicial R$", Salario_Inicial)
print("Salário Final R$" ,Salario_Final)
print("Aumento de todos os anos R$" ,Aumento)
print("Percentual total %",Percentual)


Percentual = 1.5
Salario_Inicial = float(input("Qual é o seu salário: ",))
Aumento = ( Percentual * Salario_Inicial) / 100
Salario_Final = Salario_Inicial + Aumento
Ano = 1995
while Ano <= 2021:
    Percentual = Percentual * 2
    Aumento = ( Percentual * Salario_Final) / 100
    Salario_Final = Salario_Final + Aumento
    Ano = Ano + 1
print("Salário Inicial R$%.2f"% Salario_Inicial)
print("Salário Final R$%.2f"% Salario_Final)
print("Aumento salárial total R$%.2f"% Aumento)
print("Percentual total %.1f"% Percentual)

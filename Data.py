''' Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. '''


dia = int(input("Insira um dia:", ))
mes = int(input("Insira um mês:", ))
ano = int(input("Insira um ano:", ))

if dia > 0 and dia < 32 and mes > 0 and mes < 13 and ano > 0:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12: 
        print("{}/{}/{}".format(dia, mes, ano))
   
    elif mes == 2 and dia < 30 and ((ano % 4 == 0 and ano % 100 != 0 ) or ano % 400 == 0):
        print("{}/{}/{}".format(dia, mes, ano))
    
    elif mes == 2 and dia < 29:
        print("{}/{}/{}".format(dia, mes, ano))

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia < 31:
        print("{}/{}/{}".format(dia, mes, ano))
    
    else:
        print("Data Invalida")

else:
    print("Data invalida")


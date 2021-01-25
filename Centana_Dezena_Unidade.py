#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo. 

Numero = input("Digite um número menor que 1000:")
StrNumero = str(Numero) #Para transformar os numeros digitados em uma string
QtdNumero = len(StrNumero) #Para ler quantos numeros tem na string 

if QtdNumero == 3:
    Centena = StrNumero[0]
    Dezena = StrNumero[1]
    Unidade = StrNumero[2]
    print("{} centenas, {} dezenas e {} unidades".format(Centena, Dezena, Unidade))
    
elif QtdNumero == 2:
    Dezena = StrNumero[0]
    Unidade = StrNumero[1]
    print("{} dezenas e {} unidades".format(Dezena, Unidade))
    
elif QtdNumero == 1:
    Unidade = StrNumero[0]
    print("{} unidades".format(Unidade))

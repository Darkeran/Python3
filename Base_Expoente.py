# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao 
# segundo número. Não utilize a função de potência da linguagem.                                        

Base = int(input("Digite um numero base: ",))
Expoente = int(input("Digite um número expoente: ", ))

Potencia = Base ** Expoente
print("O número {} elevado a {} é igual a {}".format(Base, Expoente, Potencia))

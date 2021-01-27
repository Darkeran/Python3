# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.                                              
  
    
numero_inteiro_1 = int ( input ( "Digite um número inteiro: "))
numero_inteiro_2 = int ( input ( "Digite um segundo número inteiro: "))
numero_real = float ( input ( "Digite um número real: "))
produto = (numero_inteiro_1 * 2) * (numero_inteiro_2 / 2)
soma = (numero_inteiro_1 * 3) + numero_real
cubo = numero_real ** 3

print ( "Este é o resultado do produto do dobro do primeiro com metade do segundo {}".format(produto))
print ( "Este é o resultado da soma do triplo do primeiro com o terceiro {}".format(soma))
print ( "Este é o resultado do número real elevado ao cubo {}".format(cubo))

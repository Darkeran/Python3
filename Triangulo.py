'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
   Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;                                                                        '''
    
    lista = []
for i in range(3):
    lados = float(input("Insira o valor do lado do triangulo:", ))
    lista.append(lados)
    lista.sort()

if lista[0] == lista[1] and lista[1] == lista[2]:
    print("Os lados do seu triangulo são iguais")

elif lista[0] < (lista[1]+lista[2]) or lista[1] < (lista[2]+lista[0]) or lista[2] < (lista[0]+lista[1]):
    
    if lista[0] != lista[1] and lista[1] != lista[2] and lista[2] != lista[0]:
        print("O seu triangulo tem 3 lados diferentes")
    
    elif lista[0] == lista[1] or lista[1] == lista[2]:
      print("Dois lados do seu triangulo são iguais")

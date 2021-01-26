''' Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
    O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50                                                                                          '''
    
loop = 0
numero = int(input("Digite um número: ",))
while loop < 10:
    loop = loop + 1
    tabuada = numero * loop
    print(numero, "x" ,loop, "=" ,tabuada)

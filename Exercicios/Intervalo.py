# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos 
# seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for 
# lido um número negativo. 

X = True
Contador_0_25 = 0
Contador_26_50 = 0
Contador_51_75 = 0
Contador_76_100 = 0

while X == True:
    Numero = int(input("Digite um número de 0 a 100: ",))
    if Numero >= 0 and Numero <= 25:
        Contador_0_25 += 1
    elif Numero >= 26 and Numero <= 50:
        Contador_26_50 += 1
    elif Numero >= 51 and Numero <= 75:
        Contador_51_75 += 1
    elif Numero >= 76 and Numero <= 100:
        Contador_76_100 += 1
    else:
        X = False
print("Entre o intervalo dos numeros 0 e 25: %s" %Contador_0_25)
print("Entre o intervalo dos numeros 26 e 50: %s" %Contador_26_50)
print("Entre o intervalo dos numeros 51 e 75: %s" %Contador_51_75)
print("Entre o intervalo dos numeros 76 e 100: %s" %Contador_76_100)

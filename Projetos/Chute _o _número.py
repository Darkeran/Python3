import random
Tentativas = 0
Numero = random.randrange(1,101)
Finalizar = 0

while Finalizar != 1:
    Chute = int(input("Chute um número de 1 a 100: ",))
    if Chute < 1 or Chute > 100:
        print("Valor Invalido")   
    elif Chute > Numero:
        print("Chutou alto, tente novamente!")
        Tentativas = Tentativas + 1 
    elif Chute < Numero:
        print("Chutou baixo, tente novamente!")
        Tentativas = Tentativas + 1 
    elif Chute == Numero:
        print("Acertou, Parabéns!")
        break
print("Você acertou depois de {} tentativas".format(Tentativas))

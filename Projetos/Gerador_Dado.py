import random
Recomecar = 0
print("Digite \n [1]SIM \n [2]NÃO")
Recomecar = int(input("Deseja jogar o dado?: ",))
if Recomecar == 2:
   print("Encerrado")
elif Recomecar != 1 and Recomecar != 2:
    print("Valor Invalido")
while Recomecar == 1:
    print("Valor do dado:",random.randrange(1, 7))
    print("Digite \n [1]SIM \n [2]NÃO")
    Recomecar = int(input("Deseja jogar novamente o dado?: ",))
    if Recomecar == 2:
        print("Encerrado")
    elif Recomecar != 1 and Recomecar != 2:
        print("Valor Invalido")

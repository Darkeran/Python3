# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7
#
# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35


Lista = []
Multiplicado = int(input("Digite o número a ser multiplicado: ",))
Multiplicador_Inicio = int(input("Digite qual o multiplicador inicial: ",))
Multiplicador_Final = int(input("Digite qual o multiplicador final: ",))

if Multiplicador_Inicio > Multiplicador_Final:
    print("O número inicial deve ser menor que o número final")
else:
    for Numero in range(Multiplicador_Inicio, Multiplicador_Final + 1 , 1):
        Tabuada = Multiplicado * Numero
        Lista.append(Tabuada)
print(Lista)

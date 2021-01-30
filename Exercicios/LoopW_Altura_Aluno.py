# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número
# do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto 
# e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
Lista_Alunos = []
Lista_Altura = []

Contador = 0
while Contador <= 9:
    Aluno = str(input("Seu Nome: "))
    Lista_Alunos.append(Aluno)
    Altura = float(input("Sua altura: ",))
    Lista_Altura.append(Altura)
    Contador = Contador + 1

Aluno_Maior = Lista_Altura.index(max(Lista_Altura))
Aluno_Maior_Cen = max(Lista_Altura)
Aluno_Menor = Lista_Altura.index(min(Lista_Altura))
Aluno_Menor_Cen = min(Lista_Altura)

print("Maior aluno: {} {} cm".format(Lista_Alunos[Aluno_Maior],Aluno_Maior_Cen))
print("Menor aluno: {} {} cm".format(Lista_Alunos[Aluno_Menor], Aluno_Menor_Cen))

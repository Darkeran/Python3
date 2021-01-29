# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
# Foram obtidos os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio. 

Lista_Cidade = []
Lista_Qtd_Carro = []
Lista_Qtd_Acidente = []
Lista_Carro_2K = []
Lista_Qtd_Acidente_2K = []
Contador = 0

while Contador < 4:
    Cidade = str(input("Nome da cidade: "))
    Carro = int(input("Número de veículos: ",))
    Acidente = int(input("Número de acidentes: ",))
    Contador = Contador + 1
    Lista_Cidade.append(Cidade)
    Lista_Qtd_Carro.append(Carro)
    Lista_Qtd_Acidente.append(Acidente)
    if Carro < 2000:
        Lista_Carro_2K.append(Carro)
        Lista_Qtd_Acidente_2K.append(Acidente)

Min_Qtd_Acidente = Lista_Qtd_Acidente.index(min(Lista_Qtd_Acidente))
Max_Qtd_Acidente = Lista_Qtd_Acidente.index(max(Lista_Qtd_Acidente))
Media_Carros = sum(Lista_Qtd_Carro) / 5
Media_Acidente_2K = (sum(Lista_Carro_2K)) / (sum(Lista_Qtd_Acidente_2K))

print("Cidade com menor quantidade de acidentes: %s "% Lista_Cidade[Min_Qtd_Acidente])
print("Cidade com maior quantidade de acidentes: %s "% Lista_Cidade[Max_Qtd_Acidente])
print("Media de carros das 5 cidades: %.2f"% Media_Carros)
print("Media de acidentes em cidades com menos de 2000 veículos: %.2f"% Media_Acidente_2K)

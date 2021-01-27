#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual 
# de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento 
# de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população 
# do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.     

Populacao_A = 8000 # 3%
Populacao_B = 200000 # 1.5%
Anos = 0

while Populacao_A < Populacao_B:
    Populacao_A = ((Populacao_A * 3) / 100) + Populacao_A
    Populacao_B = ((Populacao_B * 1.5) / 100) + Populacao_B
    Anos = Anos + 1
print("Em {} ano a Populacão A vai ultrapassar a População B".format(Anos))

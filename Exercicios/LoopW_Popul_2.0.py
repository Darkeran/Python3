# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação. 
   
População_A = int(input("População A: ",))
Taxa_Cres_A = float(input("Taxa de Crescimento da população A: ",))
População_B = int(input("População B: ",))
Taxa_Cres_B = float(input("Taxa de Crescimento da população B: ", ))
Anos = 0

while População_A < População_B:
    População_A = ((População_A * Taxa_Cres_A) / 100) + População_A
    População_B = ((População_B * Taxa_Cres_B) / 100) + População_B
    Anos = Anos + 1
print("A População A vai demorar {} anos para ultrapassar a população B".format(Anos))

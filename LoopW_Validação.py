''' Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; '''
    
    
Nome = input("Digite seu nome: ")
while len(Nome) < 3:
    Nome = input("Digite seu nome: ")

Idade = int(input("Digite sua idade: ",))   
while Idade < 1 or Idade > 150:
    Idade = int(input("Digite sua idade: ",))

Salario = float(input("Qual é o seu sálario R$:?"))                   
while Salario < 1:
    Salario = float(input("Qual é o seu sálario R$:?"))

Sexo = input("Qual é o seu sexo? \n(F)-Feminino: \n(M)-Masculino:").upper()            
while Sexo != "M" and Sexo != "F":
    Sexo = input("Qual é o seu sexo? \n(F)-Feminino: \n(M)-Masculino:").upper()

Estado_Civil = input("Estado Civil?\n(S)-Solteiro, \n(C)-Casado, \n(D)-Divorciado, \n(V)-Viúvo: ").upper()                
while Estado_Civil != "S" and Estado_Civil != "C" and Estado_Civil != "D" and Estado_Civil != "V":
    Estado_Civil = input("Estado Civil?\n(S)-Solteiro, \n(C)-Casado, \n(D)-Divorciado, \n(V)-Viúvo: ").upper()
                    
print("Nome:%s" %Nome)
print("Idade:",Idade)
print("Salario R$%.2f" %Salario)
print("Sexo:%s" %Sexo)
print("Estado Civil:%s" %Estado_Civil)

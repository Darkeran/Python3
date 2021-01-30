# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str  (input("Digite (F)-Feminino ou (M)-Masculino: ").upper())

if sexo == "M":
    print("Seu sexo é masculino")
    
elif sexo == "F":
    print("Seu sexo é feminino")
    
else:
    print("Sexo invalido")

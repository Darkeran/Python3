# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.                                     


loop = 1
while loop > 0:
    login = input("Digite um nome de usuario: ")
    senha = input("Digite uma senha: ")
    if login == senha:
        print("O nome do usuário não pode ser igual a senha!")
    else:
        print("Usuario cadastrado")
        break

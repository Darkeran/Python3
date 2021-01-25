''' Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
    Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
    Caso contrário, ele será classificado como "Inocente".                                                                                    '''
Lista = []

print("Apenas digite sim ou não para as proximas perguntas")

Telefone = input("Você telefonou para a vítima?:").upper()
Lista.append(Telefone)

Local = input("Você esteve no local do crime?:").upper()
Lista.append(Local)

Morar = input("Você mora perto da vítima?:").upper()
Lista.append(Morar)

Dever = input("Você devia para a vítima?:").upper()
Lista.append(Dever)

Trabalhar = input("Voçê ja trabalhou com a vitima?:").upper()
Lista.append(Trabalhar)


Qtd_sim = Lista.count("SIM")

if Qtd_sim == 5:
    print("Voçê é o assassino")
elif Qtd_sim == 3 or Qtd_sim == 4:
    print("Voçê é cumplice")
elif Qtd_sim == 2 :
    print("Voçê é suspeito")
else:
    print("Voçê é inocente")


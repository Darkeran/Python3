# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite qualquer letra:" ).upper())

if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U" :
    print("A letra {} é uma vogal".format(letra))
    
else:
    print("A letra {} é uma consoante".format(letra))

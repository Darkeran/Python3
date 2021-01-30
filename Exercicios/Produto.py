# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato

produto1 = float(input("Digite o preço em R$ do primeiro produto:", ))
produto2 = float(input("Digite o preço em R$ do segundo produto:", ))
produto3 = float(input("Digite o preco em R$ do terceito produto:", ))

if produto1 < produto2 and produto1 < produto3:
    print("O Primeiro produto é o mais em conta dos três produtos")
    
elif produto2 < produto1 and produto2 < produto3:
    print("Segundo produto é o mais em conta dos três produtos")
    
elif produto3 < produto1 and produto3 < produto2:
    print("O Terceiro produto é o mais em conta dos três produtos")

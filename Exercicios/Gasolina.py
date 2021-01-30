#  Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#
#  Álcool:
#  até 20 litros, desconto de 3% por litro
#  acima de 20 litros, desconto de 5% por litro
#  Gasolina:
#  até 20 litros, desconto de 4% por litro
#  acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, 
#  o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente 
#  sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.                             
    
    
Tipo_Combustivel = input("Digite (G) Para Gasolina ou (A) Para Álcool:" ).upper()
Qtd_Litros = float(input("Quantos Litros de combustivel: "))

if Tipo_Combustivel == "G":
    if Qtd_Litros > 20:
        Desconto = (Qtd_Litros * 2.50) / 6
        Preco_Pagar = (Qtd_Litros * 2.50) - Desconto    
    else:
        Desconto = (Qtd_Litros * 2.50) / 4
        Preco_Pagar = (Qtd_Litros * 2.50) - Desconto
    Tipo_Combustivel = "Gasolina"

elif Tipo_Combustivel == "A":
    if Qtd_Litros > 20:
        Desconto = (Qtd_Litros * 1.90) / 5
        Preco_Pagar = (Qtd_Litros * 1.90) - Desconto
    else:
        Desconto = (Qtd_Litros * 1.90) / 3
        Preco_Pagar = (Qtd_Litros * 1.90) - Desconto
    Tipo_Combustivel = "Àcool"

print("Tipo do Combustivel %s" %Tipo_Combustivel)
print("Desconto %.2f" %Desconto)
print("Total a pagar %.2f" %Preco_Pagar)


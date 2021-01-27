#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                          Até 5 Kg           Acima de 5 Kg
#    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

#    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
#   receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade 
#   (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. 
    
Pedido_Maca = float(input("Quantos Kg de maça?: ",))
Pedido_Morango = float(input("Quantos Kg de Morango?: ",))

Total_Maca = Pedido_Maca * 1.80
Total_Morango = Pedido_Morango * 2.50

Pedido_Total = Pedido_Maca + Pedido_Morango
Total_Pagar = Total_Morango + Total_Maca

if Pedido_Total > 8 or Total_Pagar > 25:
    Desconto_Maca = (Total_Maca * 1.50) / 100
    Desconto_Morango = (Total_Morango * 2.20) / 100

    Total_Maca = Total_Maca * 1.50 + Desconto_Maca
    Total_Morango = Total_Morango * 2.0 + Desconto_Morango
    Total_Pagar = Total_Maca + Total_Morango

    print("Total Maca R$%.2f" %Total_Maca)
    print("Total Morango R$%.2f" %Total_Morango)
    print("Total a ser pago R$%.2f" %Total_Pagar)
    print("Total de Maca %.1fKg" %Pedido_Maca)
    print("Total de Morango %.1fKg" %Pedido_Morango)


else:
    print("Total Maca R$%.2f" %Total_Maca)
    print("Total Morango R$%.2f" %Total_Morango)
    print("Total a ser pago R$%.2f" %Total_Pagar)
    print("Total de Maca %.1fKg" %Pedido_Maca)
    print("Total de Morango %.1fKg" %Pedido_Morango)

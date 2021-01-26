''' O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
    porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o 
    cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo 
    e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
    tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.      '''
    
    
Tipo_Carne = str(input("Qual carne você vai levar alcatra, picanha ou file duplo?:" )).lower()

if Tipo_Carne == "file duplo":
  Qtd_Carne = float(input("Quantos Kg ?:",))
  if Qtd_Carne > 5:
    Preco_Carne = Qtd_Carne * 5.80
    Tipo_Pagamento = str(input("Pagamento cartão tabajara ou dinheiro ?:" )).lower()
    if Tipo_Pagamento == "cartão" or Tipo_Pagamento == "cartao":
      Desconto = (Preco_Carne * 5) / 100
      Preco_Carne_Final = Preco_Carne - Desconto
  elif Qtd_Carne > 0 and Qtd_Carne < 5:
    Preco_Carne = Qtd_Carne * 4.90
    Tipo_Pagamento = str(input("Pagamento cartão tabajara ou dinheiro ?:" )).lower()
    if Tipo_Pagamento == "cartão" or Tipo_Pagamento == "cartao":
      Desconto = (Preco_Carne * 5) / 100
      Preco_Carne_Final = Preco_Carne - Desconto

elif Tipo_Carne == "alcatra":
  Qtd_Carne = float(input("Quantos Kg ?:",))
  if Qtd_Carne > 5:
    Preco_Carne = Qtd_Carne * 6.80
    Tipo_Pagamento = str(input("Pagamento cartão tabajara ou dinheiro ?:" )).lower()
    if Tipo_Pagamento == "cartão" or Tipo_Pagamento == "cartao":
     Desconto = (Preco_Carne * 5) / 100
     Preco_Carne_Final = Preco_Carne - Desconto  
  elif Qtd_Carne > 0 and Qtd_Carne < 5:
    Preco_Carne = Qtd_Carne * 5.90
    Tipo_Pagamento = str(input("Pagamento cartão tabajara ou dinheiro ?:" )).lower()
    if Tipo_Pagamento == "cartão" or Tipo_Pagamento == "cartao":
      Desconto = (Preco_Carne * 5) / 100
      Preco_Carne_Final = Preco_Carne - Desconto

elif Tipo_Carne == "picanha":
  Qtd_Carne = float(input("Quantos Kg ?:",))
  if Qtd_Carne > 5:
    Preco_Carne = Qtd_Carne * 7.80
    Tipo_Pagamento = str(input("Pagamento cartão tabajara ou dinheiro ?:" )).lower()
    if Tipo_Pagamento == "cartão" or Tipo_Pagamento == "cartao":
      Desconto = (Preco_Carne * 5) / 100
      Preco_Carne_Final = Preco_Carne - Desconto
  elif Qtd_Carne > 0 and Qtd_Carne < 5:
    Preco_Carne = Qtd_Carne * 6.90
    Tipo_Pagamento = str(input("Pagamento cartão tabajara ou dinheiro ?:" )).lower()
    if Tipo_Pagamento == "cartão" or Tipo_Pagamento == "cartao":
     Desconto = (Preco_Carne * 5) / 100
     Preco_Carne_Final = Preco_Carne - Desconto


print(Tipo_Carne)
print(Qtd_Carne,"Kg")
print("R$%.2f" %Preco_Carne)
print("Tipo de Pagamento: %s" %Tipo_Pagamento)
print("Desconto R$:%.2f" %Desconto)
print("Valor final R$:%.2f" %Preco_Carne_Final)

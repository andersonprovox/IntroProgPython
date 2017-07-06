#Faça um programa que calcule o percentual de desconto e exiba o desconto e preço a pagar

preco = float(input("Digite o valor do produto: "))
perDesconto = float(input("Digite o percentual de desconto: "))


valorPagar = preco - (preco * perDesconto / 100)
valorDesconto = preco * perDesconto / 100

print("valor do produto sem desconto R$ %5.2f" % preco)
print("Valor do desconto R$ %5.2f" % valorDesconto)
print("Valor total a pagar com desconto R$ %5.2f" % valorPagar)
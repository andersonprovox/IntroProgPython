# Cálculo de média usando acumulador

x = 1
soma = 0
while x<= 5:
    n = int(input("%d Digite o número:" % x))
    soma += n
    x += 1
print("Média: %5.2f" % (soma/5))

#Soma de 10 números
n = 1
soma = 0
while n <= 10:
    x = int(input("Digite %d número: " % n))
    soma += x
    n += 1
print("Soma: %d" % soma)

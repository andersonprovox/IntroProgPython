'''Exercício onde o algoritmo deve fazer a mesma função de uma operação de divisão usando 
somente a operação de subtração'''

print("Insira os números para a divisão")

x = int(input("Insira o primeiro número: "))
dividendo = x
y = int(input("Insira o segundo número: "))

res = 0
if x >= y:
    while x>= y:
        x = x - y
        res += 1
    print("%d / %d = %d" % (dividendo, y, res))
else:
    print("Não há como dividir com o dividendo sendo menor que o divisor")
#print("%d / %d = %d" % (dividendo, y, res))
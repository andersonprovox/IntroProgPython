
'''Exercicio onde o algoritmo deve fazer uma operação de multiplicação somente usando a operação de somar'''
print("Insira números para a operação matemática")
x = int(input("Insira o primeiro número: "))
y = int(input("Insira o segundo número: "))

cont = 1
resul = 0

while cont <= y:
    resul += x
    cont+=1
print("%d * %d = %d" % (x, y, resul))
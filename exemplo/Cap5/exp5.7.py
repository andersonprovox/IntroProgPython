#Impressão de números pares até o número definido pelo usuário
fim = int(input("Digite o último número a imprimir: "))
x = 0
while x <= fim:
    if x % 2 == 0:
        print(x)
    x += 1
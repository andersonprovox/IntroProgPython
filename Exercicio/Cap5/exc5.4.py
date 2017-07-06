# Alterar programa do exp5.8 iciando a contagem em pares a partir do 1

fim = int(input("Digie o último número a imprimir:"))
x = 1
while x <= fim:
    if x % 2 == 0:
        print(x)
    x += 1

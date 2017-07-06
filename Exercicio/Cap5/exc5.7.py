n = int(input("Insira a tabuada que quer: "))
x = int(input("Inicio da tabuada: "))
y = int(input("Fim da tabuada: "))
while x <= y:
    print("%d x %d = %d" % (n, x, n * x))
    x += 1

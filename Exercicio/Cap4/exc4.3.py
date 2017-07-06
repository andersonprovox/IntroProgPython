#Saída informe o maior e o menor número de 3 números
#Entrada: inserir 3 números
#Processamento: comparar 3 números e escolher o maior e o menor

a = int(input("Insira o 1º número: "))
b = int(input("Insira o 2º número: "))
c = int(input("Insira o 3º número: "))

if c < b:
    if c < a:
        print("O 3º número é o menor valor: %d" % c)
elif b < a:
    print("o 1º Número é o maior valor: %d" % a)
#Saida: converter a temperatura em C° para F°
# Entrada: a temperatura em C°
#Processamento: usar a formula de conversão:
# f = (9 x c) / 5 + 32

celsius = float(input("Insira a temperatura em Celsius: "))


f = (9 * celsius) /5 + 32

print("A conversão em Fahrenheit: %5.2f" % f)

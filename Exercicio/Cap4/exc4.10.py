#Programa para calcular o valor a pagar de energia elétrica de acordo com o tipo de instalação

kwh = int(input("Insira o total de Energia consumidos: "))
tipoins = input("Informe o tipo de instalação: R - Residencias| I - Industrias | C - comércios: ")

if tipoins == "R" and kwh <= 500:
    total = kwh * 0.40
    print("total a pagar: %5.2f" % total)
elif tipoins == "R" and kwh > 500:
    total = kwh * 0.65
    print("total a pagar: %5.2f" % total)
elif tipoins == "I" and kwh <= 1000:
    total = kwh * 0.55
    print("total a pagar: %5.2f" % total)
elif tipoins == "I" and kwh > 1000:
    total = kwh * 0.60
    print("total a pagar: %5.2f" % total)
elif tipoins == "C" and kwh <= 5000:
    total = kwh * 0.55
    print("total a pagar: %5.2f" % total)
elif tipoins == "C" and kwh > 5000:
    total = kwh * 0.60
    print("total a pagar: %5.2f" % total)
else:
    print("Entrada do tipo de instalação inválida")
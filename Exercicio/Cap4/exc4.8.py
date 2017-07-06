#Saída: apresentar o resultado da operação matemática solicitada
#Entrada: dois números e o tipo de operação que deseja que seja efetuada
#Processamento: faça a operação básica (+ - * /) de acordo com a opção escolhida pelo usuário

numero1 = float(input("Digite o primeiro numero "))
numero2 = float(input("Digite o segundo número "))
print("Informe qual operação matemática deseja fazer:")
operacao = int(input("1 - Adição|2 - para Subtração|3 - Multiplicação| 4 - Divisão: "))


if operacao == 1:
    print("%5.2f + %5.2f = %5.2f" %(numero1, numero2, numero1 + numero2))
elif operacao == 2:
    print("%5.2f - %5.2f = %5.2f" % (numero1, numero2, numero1 - numero2))
elif operacao == 3:
    print("%5.2f * %5.2f = %5.2f" % (numero1, numero2, numero1 * numero2))
elif operacao ==4:
    print("%5.2f / %5.2f = %5.2f" % (numero1, numero2, numero1 / numero2))
else:
    print("Opção invalida!")

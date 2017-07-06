#Saída: mostrar o valor da prestação o valor da casa e quandos meses a pagar, como também se o valor da prestação execer 30%
#Entrada: perguntar o valor da casa, salario do comprador e a quantidade de anos a pagar
#Processamento: calcular o valor da prestação como sendo o da casa dividido pelo número de meses a pagar o valor da prestação
#não pode exceder 30% do salário

valorCasa = float(input("Informe o valor do imóvel: "))
salario = float(input("Informe o salário do comprador: "))
anos = int(input("Informe a quantidade de anos a pagar: "))

parcela = valorCasa / (anos * 12)
partSal = salario * 0.30
if partSal > parcela:
    print("Valor da parcela: %5.2f" % parcela)
    print("Valor da casa: %5.2f" % valorCasa)
    print("Meses a pagar: %d" % (anos * 12))
else:
    print("O valor da parcela execedeu 30% do teu salário")
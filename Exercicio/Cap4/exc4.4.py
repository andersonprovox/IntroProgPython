#Saída: Salário aumentado em 10% para os maiores que 1250 e em 15% para os menores que 1250
#Entrada: o salario de um funcionário
#Processamento: se o salário for maior que 1250 aumente para 10% se o salario for menor aumente para 15%

salario = float(input("Insira o seu salário: "))

if salario > 1250.00:
    aumento = salario + (salario * 0.10)
else:
    aumento = salario + (salario * 0.15)
print("O seu aumento salarial foi de R$%6.2f" % aumento)
print("Salario atual R$%6.2f" % salario)

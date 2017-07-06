#Solicitar o valor de um salário e mostra o valor do aumento do novo salario
salario = float(input("insira o salário "))
aumento = float(input("Insira a porcentagem de aumento: "))


print("Salario atual R$ %5.2f" %salario)
print("Aumento R$ %5.2f"%(salario * aumento/100))
print("Salário total de R$ %5.2f"%(salario + (salario * aumento/100)))
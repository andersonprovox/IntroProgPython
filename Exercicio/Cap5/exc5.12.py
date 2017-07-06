deposito = float(input("Insira o valor do depósito inicial: "))
juros = float(input("Insira o valor do juros: "))
depMensal = 0
mes = 1
while mes <= 24:
    totalGanho = deposito  * (juros /100)
    deposito + depMensal
    deposito += totalGanho
    print("mês %d : R$ %5.2f" % (mes, deposito))
    mes += 1
    depMensal = float(input("Qual o valor que será depositado no mês %d: " % mes))
print("Total ganho em 24 meses R$ %5.2f" % totalGanho)
'''não está funcionando corretamente em questão de soma'''
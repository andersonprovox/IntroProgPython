'''saída: exibir os valores mês a mês dos 24 meses
          escreva o total ganho com juros no período
    entrada: deposito incial e taxa de juros de uma poupança
    processamento: calcular o ganho dos juros mensalmente
                    soma os ganhos com juros no período'''

deposito = float(input("Insira o valor do depósito: "))
juros = float(input("Insira o valor do juros: "))

mes = 1
while mes <= 24:
    totalGanho = deposito * (juros /100)
    deposito += totalGanho
    print("mês %d : R$ %5.2f" % (mes, totalGanho))
    mes += 1
print("Total ganho em 24 meses R$ %5.2f" % totalGanho)
'''saída: mostre o número  de meses para que um a dívida  seja  paga o total e o total de juros pago
    entrada: pergunte o valor incial de uma dívida e o juros mensal'''

dividaInicial = float(input("insira o valor da dívida: "))
juroMes = float(input("Insira o juro mensal: "))
valorMensal = float(input("Insira o valor mensal para pagar: "))

pgtoEfetuado = 0
meses = 0
jurosTrasn = juroMes/100
jurosTotal = 0
dividaTotal = dividaInicial + (dividaInicial * jurosTrasn)

while pgtoEfetuado < dividaTotal:

    jurosTotal += dividaInicial * jurosTrasn
    pgtoEfetuado += valorMensal
    meses += 1

print("Valor total da dívida R$ %5.2f " % dividaTotal)
print("Total pago R$ %5.2f" % pgtoEfetuado)
print("Total de Juros Pagos R$ %5.2f" % jurosTotal)
print("Total de meses para pagar: %d" % meses)


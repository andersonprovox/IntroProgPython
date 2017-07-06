#saida: calcular o preço a pagar do aluguel do dia e o km rodado
#entrada: dias de aluguel e km rodada
#Processamento: multiplicar por 60 reais o valor do dia, multiplicar po 0.15 centavos
# o valor de kilometro rodado

dias = int(input("Digite a quantidade de dias em que o carro ficou alugado: "))
km = float(input("Digite a quantidade de Km Rodados com o carro: "))

totalDias = dias * 60.00
totalKm = km * 0.15

print("O total de dias alugados: %d" %dias)
print("O total a pagar de dias %5.2f" %totalDias)
print("O total de Km rodado: %5.2f" %km)
print("total a pagar de Km rodado: %5.2f" %totalKm)
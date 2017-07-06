#programa para calcular o total em dias, horas, minutos e segundos e calcular tudo em segundos

dia = int(input("Digite o total de dias: "))
hora = int(input("digite o total de horas: "))
minuto = int(input("digite o total de minutos: "))
segundo = int(input("digite o total de segundos: "))

segundo += dia * 24 * 60 * 60
segundo += hora * 60 * 60
segundo += minuto * 60

print("O total em segundos é: %d" % segundo)
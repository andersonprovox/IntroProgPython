#Saída: exibir mensagem de multado se o motorista ultrapassar 80km/h
# exibir o valor da multa se cobrando 5,00 por cada km acima de 80
#Entrada: a velocidade do carro do usuário
#Processamento: verificar se o carro passou de 80km/h se sim calcular o total de
# km excedente e adicionar na multa 5 reais por km a mais

velocidade = int(input("Informe a velocidade do usuário: "))

if velocidade > 80:
    multa = (velocidade - 80) * 5.00
    print("Você foi multado!, a Km excedente foi de: %d , total a pagar de R$%5.2f" % (velocidade-80, multa))
else:
    print("Não multas para o usuário.")

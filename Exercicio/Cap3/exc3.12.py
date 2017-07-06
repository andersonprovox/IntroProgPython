#saida: calcular o tempo de viagem de um carro
#entrada: a distançia a percorrer e a velocidade média
#Processamento: calcular a distancia a percorrer e a velociade média(Tempo = Vm * Distância

distant = float(input("Digite a distância a percorrer: "))
velmed = float(input("Digite a Velocidade Média: "))

hora = distant / velmed
minuto = hora * 60
segundo = minuto * 60

print("O tempo de viagem é de: %d hora - %d minuto - %d segundo" %(hora, minuto, segundo))
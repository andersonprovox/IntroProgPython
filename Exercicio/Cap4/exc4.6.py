#Saída:Mostrar o preço da passagem por km
#Entrada: perguntar a distância que o usuário deseja percorrer
#Processamento: se for até 200 km cobre 0,50 centavos por cada
#se for maior cobre 0,45 por cada km.

distancia = int(input("informe a distância que deseja percorrer: "))

if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print("o valor de uma passagem é R$%6.2f para uma distância de %d" % (passagem, distancia))

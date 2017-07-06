'''Saida: mostrar os 10 primeiros multiplos de 3
entrada: nenhuma
Processamento: multiplicar 10 números por 3 use um contador para isso.'''

cont = 1
multiplo = 3
print("Veja o múltiplo de %d: " % multiplo)
while cont <= 10:
    multiplo += 3
    print(multiplo)
    cont += 1

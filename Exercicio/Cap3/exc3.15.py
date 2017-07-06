#saída: exiba em dias o total de tempo de vida que um fumante perdeu
#Entrada: a quantidade de cigarros fumados por dia e quantos anos fumando
#processamento: um fumante perde 10 min de sua vida a cada cigarro

cigarros = int(input("informe quantos cigarros vocẽ fuma; "))
anos = float(input("Há quantos anos fuma? "))


dias = anos * 365
dias += ((cigarros * 10) /60) /24

print("Que pena! Você já perdeu %d dias de vida!" % dias)
#exemplo usando estruturas aninhadas
# é importante no caso de que quando temos mais de uma acondição a ser verificada
# e quando para executar uma ação precisamos validar mais de uma ação

minutos = int(input("Quantos minutos você utilizou este mês: "))
if minutos <200:
    preco = 0.20
else:
    #Este if com recuo(identação) dentro do if é uma estrutura aninhada
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15
#Aqui está sendo calculado os preços dentro do print
print("Você vai pagar este mês: R$%6.2f" % (minutos * preco))

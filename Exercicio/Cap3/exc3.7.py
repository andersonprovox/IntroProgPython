
#programa que solicita dois numeros inteiros e imprime a sua soma
#armazenando um tipo inteiro na variável e usando o conversor para atribuir
#um numero inteiro caso contrário por padrão atribui uma string
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

resultado = a + b
#no momento onde usa-se os marcadores para exibir os valores das variáveis
# quando houver mais de uma variável atribua a porcentagem e as variáveis em parentesis
print("a soma de %d + %d = %d" % (a, b, resultado))
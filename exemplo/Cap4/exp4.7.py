#estrutura com vários ifs aninhados veja que a leitura fica um pouco mais difícil
#estou usando variáveis sem acentuação ou letras especiais como o 'ç' isso porque
#em outras linguagens dá erro então por padronização não uso isso em python por
#mais que seja possível dentro das convenções da linguagem

categoria = int(input("Digite a categoria do produto:"))
if categoria == 1:
    preco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else:
                    print("Categoria inválida, digite um valor entre 1 e 5!")
                    preco = 0
print("O preço do produto é: R$%6.2f" % preco)

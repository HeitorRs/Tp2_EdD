def contar_livros_impares(fila):
    contador = 0

    for id_livro in fila:
        if id_livro % 2 != 0:
            contador += 1
    
    return contador

fila_livros = [101, 102, 103, 104, 105, 106, 107]
resultado = contar_livros_impares(fila_livros)
print("Número de livros com ID ímpar:", resultado)
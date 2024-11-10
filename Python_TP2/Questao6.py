def contar_pedidos_impares(pilha):
    contador = 0

    while pilha:
        elemento = pilha.pop()
        if elemento % 2 != 0:
            contador += 1
    return contador


pilha_pedidos = [111, 112, 113, 114, 115, 116, 117, 118, 119]
resultado = contar_pedidos_impares(pilha_pedidos)
print("A quantidade de pedidos com número de identificação ímpar é:", resultado)
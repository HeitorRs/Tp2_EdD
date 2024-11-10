def ordenar_notas(pilha):
    pilha_auxiliar = []

    while pilha:
        nota = pilha.pop()

        while pilha_auxiliar and pilha_auxiliar[-1] < nota:
            pilha.append(pilha_auxiliar.pop())

        pilha_auxiliar.append(nota)

    while pilha_auxiliar:
        pilha.append(pilha_auxiliar.pop())

    return pilha
notas = [4, 2, 8, 7, 1, 3, 9]
print("Pilha notas original:", notas)
notas_ordenadas = ordenar_notas(notas)
print("Pilha notas ordenada:", notas_ordenadas)
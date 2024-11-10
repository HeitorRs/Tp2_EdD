def encontrar_duplicados_bruto(lista):
    duplicados = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j] and lista[i] not in duplicados:
                duplicados.append(lista[i])
    return duplicados


lista = [1, 2, 3, 4, 2, 5, 6, 7, 1]
duplicados = encontrar_duplicados_bruto(lista)
print("Números duplicados:", duplicados)
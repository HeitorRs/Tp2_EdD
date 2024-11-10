def encontrar_duplicados_conjunto(lista):
    vistos = set()
    duplicados = []

    for numero in lista:
        if numero in vistos:
            duplicados.append(numero)
        else:
            vistos.add(numero)

    return duplicados


lista = [1, 2, 3, 3, 4, 2, 5, 6, 7, 1]
duplicados = encontrar_duplicados_conjunto(lista)
print("Números duplicados:", duplicados)
def ordenar_fila(fila):
    n = len(fila)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    
    return fila

fila_numeros = [31, 44, 5, 33, 123, -79, 0, 27, -9]
fila_ordenada = ordenar_fila(fila_numeros)
print("Fila ordenada:", fila_ordenada)
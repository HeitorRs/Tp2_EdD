def inverter_fila(fila):
    inicio = 0 
    fim = len(fila) - 1
    
    while inicio < fim:
        fila[inicio], fila[fim] = fila[fim], fila[inicio]
        
        inicio += 1
        fim -= 1
    
    return fila

fila_pacientes = ["Paciente 1", "Paciente 2", "Paciente 3", "Paciente 4", "Paciente 5"]
inverter_fila(fila_pacientes) #tambem poderia usar o reverse()
print("Fila invertida:", fila_pacientes)
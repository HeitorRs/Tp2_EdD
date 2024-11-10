def tarefa_no_topo(pilha_de_tarefas):
    if not pilha_de_tarefas:
        return 'Sem tarefas a fazer :)'  
    
    return pilha_de_tarefas[-1]

pilha_tarefas = ["preparar janta", "Lavar roupa", "Ir ao mercado"]
tarefa_atual = tarefa_no_topo(pilha_tarefas)
print("A tarefa mais recente (no topo) é:", tarefa_atual)
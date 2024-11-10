class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def hash(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self.hash(chave)
        for par in self.tabela[indice]:
            if par[0] == chave:
                par[1] = valor
                return
        self.tabela[indice].append([chave, valor])
        print(f"Chave {chave} inserida com valor {valor}.")

    def buscar(self, chave):
        indice = self.hash(chave)
        for par in self.tabela[indice]:
            if par[0] == chave:
                return par[1]
        return f"Chave {chave} não encontrada."

    def remover(self, chave):
        indice = self.hash(chave)
        for i, par in enumerate(self.tabela[indice]):
            if par[0] == chave:
                del self.tabela[indice][i]
                print(f"Chave {chave} removida.")
                return
        print(f"Chave {chave} não encontrada.")


tabela = TabelaHash(10)

tabela.inserir("nome", "João")
tabela.inserir("idade", 30)
tabela.inserir("cidade", "São Paulo")
tabela.inserir("nome", "Heitor")

print(tabela.buscar("nome"))
print(tabela.buscar("idade"))
print(tabela.buscar("cidade"))
print(tabela.buscar("endereco"))


tabela.remover("idade")
print(tabela.buscar("idade"))

tabela.remover("endereco") 
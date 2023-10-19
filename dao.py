from controller import*

class ToDO:
    def __init__(self, arquivo="tarefas.txt"):
        self.arquivo = arquivo
        self.lista = []
        self.loadTarefas()

    def addTarefa(self, tarefa):
        try:
            with open(self.arquivo, "a") as file:
                file.write(f"{len(self.lista) + 1} {tarefa}\n")
            self.loadTarefas()
            return True
        except Exception as e:
            print(f"Erro ao adicionar tarefa: {e}")
            return False

    def removeTarefa(self, excluir):
        try:
            with open(self.arquivo, "w") as file:
                file.write("ID - Tarefa\n")
                nova_lista = [tarefa for i, tarefa in enumerate(self.lista) if i != excluir]
                for i, tarefa in enumerate(nova_lista):
                    file.write(f"{i + 1} {tarefa}\n")
            self.loadTarefas()
            return True
        except Exception as e:
            print(f"Erro ao excluir tarefa: {e}")
            return False
        

    def listarTarefa(self):
        return self.lista

    def loadTarefas(self):
        try:
            with open(self.arquivo, "r") as file:
                self.lista = [linha.strip().split(' ')[1] for linha in file.readlines()[1:]]
        except FileNotFoundError:
            with open(self.arquivo, "w") as file:
                file.write("ID - Tarefa\n")

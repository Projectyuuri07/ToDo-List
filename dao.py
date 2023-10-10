from controller import*

class ToDO:
    def __init__(self, arquivo="tarefas.txt"):
        self.arquivo = arquivo
        self.lista = []
        self.loadTarefas()

    def addTarefa(self, tarefa):
        try:
            with open(self.arquivo, "a") as file:
                file.write(f"{len(self.lista) + 1};{tarefa}\n")
            self.loadTarefas()
            return True
        except Exception as e:
            print(f"Erro ao adicionar tarefa: {e}")
            return False






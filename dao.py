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

    def removeTarefa(self, index):
        try:
            with open(self.arquivo, "r") as file:
                tarefas = file.readlines()

            if 0 <= index < len(tarefas):
                del tarefas[index]

                with open(self.arquivo, "w") as file:
                    for i, linha in enumerate(tarefas, start=1):
                        file.write(f"{i};{linha.split(';', 1)[1]}")

                self.loadTarefas()
                return True
            else:
                raise ValueError("Número de tarefa a excluir fora do alcance")
        except Exception as e:
            print(f"Erro ao excluir tarefa: {e}")
            return False

    def listarTarefa(self):
        return self.lista

    def loadTarefas(self):
        try:
            with open(self.arquivo, "r") as file:
                self.lista = [linha.strip().split(';')[1] for linha in file.readlines()]
        except FileNotFoundError:
            open(self.arquivo, "w").close()


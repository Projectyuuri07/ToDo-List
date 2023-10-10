from model import*
from view import*

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
        self.tarefa = tarefa
        try:
            todo.addTarefa(self.tarefa)
            print("Tarefa adicionada com sucesso")
        except Exception as e:
            print(f"Erro ao adicionar tarefa: {e}")
        print("")  

class ControllerExcluirTarefa():
    def __init__(self, excluir):
        try:
            excluir = int(excluir) - 1
            if excluir < 0:
                raise  ("Digite um número inteiro positivo para excluir a tarefa")
            if excluir >= len(todo.lista):
                raise ("Número de tarefa a excluir fora do alcance")
            todo.removeTarefa(excluir)
            print("Tarefa excluída com sucesso")
        except Exception as erro:
            print(f"Erro ao excluir tarefa: {erro}")


class ControllerListarTarefa():
    def __init__(self):
        try:
            ControllerLista = todo.listarTarefa()
            if not ControllerLista:
                print("Nenhuma tarefa encontrada.")
            else:
                cont = 1
                for tarefa in ControllerLista:
                    print(f"{cont} -- {tarefa}")
                    cont += 1
        except Exception as erro:
            print(f"Erro: {erro}")

todo = ToDO()

def obter_opcao():
        opcao = input("Digite a opção desejada: ")
        if opcao.isdigit():
            return int(opcao)
        else:
            print("Por favor, digite um número inteiro válido.")

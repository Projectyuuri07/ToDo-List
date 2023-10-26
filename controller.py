from model import *
from dao import *


class ControllerAdicionarTarefa:
    def __init__(self, tarefa):
        self.tarefa = tarefa
        if len(self.tarefa) == 0:
            print("Digite uma tarefa válida")
        else:
            try:
                adicionar_tarefa(self.tarefa)
                print("Tarefa adicionada com sucesso")
            except Exception as e:
                print(f"Erro ao adicionar tarefa: {e}")
            print("")


class ControllerExcluirTarefa:
    def __init__(self, excluir):
        try:
            excluir = int(excluir)
            if excluir <= 0:
                print(
                    "Digite um número inteiro positivo maior que zero para excluir uma tarefa"
                )
            elif excluir >= len(listar_tarefas()):
                print("Número de tarefa a excluir fora do alcance")
            else:
                excluir_tarefas(excluir)
                print("Tarefa excluída com sucesso")
        except Exception as e:
            print(f"Ops! Ocorreu um erro {e}")


class ControllerListarTarefa:
    def __init__(self):
        try:
            listar_tarefas()
        except Exception as erro:
            print(f"Erro: {erro}")


class ControllerConcluirTarefa:
    def __init__(self, tarefa):
        tarefa = int(tarefa)
        concluir_tarefa(tarefa)


class ControllerAlterarTarefa:
    def __init__(self, alterar):
        try:
            alterar = int(alterar)
            if alterar <= 0:
                print(
                    "Digite um número inteiro positivo maior que zero para alterar uma tarefa"
                )
            elif alterar >= len(listar_tarefas()):
                print("Número de tarefa a alterar fora do alcance")
            else:
                try:
                    alterar_tarefa(alterar)
                except Exception as erro:
                    print(f"Erro: {erro}")
                print("Tarefa alterada com sucesso")
        except Exception as e:
            print(f"Ops! Ocorreu um erro {e}")


class ControllerListaConcluidos:
    def __init__(self):
        try:
            listar_tarefas_concluidas()
        except Exception as e:
            print(f"Ops! Ocorreu um erro {e}")


todo = ToDO()


def eh_numero_inteiro(s):
    try:
        int(s)
        return True

    except ValueError:
        return False


def obter_opcao():
    while True:
        opcao = input("Digite a opção desejada: ")
        if eh_numero_inteiro(opcao):
            return int(opcao)
        else:
            print("Por favor, digite um número inteiro válido.")
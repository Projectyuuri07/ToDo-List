from controller import *

sair = True

while sair == True:
    print("SOFTWARE DE GERENCIAMENTO DE TAREFAS")
    print(
        " [1] -> Adicionar tarefa\n [2] -> Listar tarefas\n [3] -> Alterar tarefas\n [4] -> Concluir Tarefa\n [5] -> Listar tarefas concluidas\n [6] -> Excluir tarefa\n [7] -> Sair\n"
    )

    opcao = obter_opcao()

    match opcao:
        case 1:
            limpar()
            tarefa = input("Digite a tarefa: ")
            adicionartarefa = ControllerAdicionarTarefa(tarefa)
            parar()
            limpar()

        case 2:
            limpar()
            print("--| Lista de Tarefas do arquivo To-do.txt|-- ")
            print("")
            listar_tarefas()
            print("")
            parar()
            limpar()
        case 3:
            limpar()
            print("--| Lista de Tarefas do arquivo To-do.txt|-- ")
            listarTarefa = ControllerListarTarefa()
            alterar = input("\nDigite o número da tarefa que deseja alterar: ")
            alterarTarefa = ControllerAlterarTarefa(alterar)
            parar()
            limpar()
        case 4:
            limpar()
            print("--| Lista de Tarefas do arquivo To-do.txt|-- ")
            listarTarefa = ControllerListarTarefa()
            concluir = input("\nDigite o Id da tarefa que quer concluir: ")
            limpar()
            ConcluirTarefa = ControllerConcluirTarefa(concluir)
            listarTarefa = ControllerListarTarefa()
            parar()
            limpar()
        case 5:
            limpar()
            ListarTarefasConcluidas = ControllerListaConcluidos()
            parar()

        case 6:
            limpar()
            print("--| Lista de Tarefas do arquivo To-do.txt|-- ")
            listarTarefa = ControllerListarTarefa()
            excluir = input("Digite o número da tarefa que deseja excluir: ")
            excluirTarefa = ControllerExcluirTarefa(excluir)
            limpar()
            print("--| Nova Lista de Tarefas |--")
            listarTarefa = ControllerListarTarefa()
            parar()
            limpar()
        case 7:
            limpar()
            print("Saindo...")
            parar()
            sair = False
        case _:
            limpar()
            print("Opção inválida")
            print("")
            parar()
            limpar()
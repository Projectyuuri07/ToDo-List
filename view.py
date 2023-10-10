from controller import*

sair=True

while sair == True:
    limpar()
    print("\nSOFTWARE DE GERENCIAMENTO DE TAREFAS")
    print(" [1]Adicionar tarefa\n [2] Excluir tarefa\n [3] Listar tarefas\n [00] Sair")
    opcao = obter_opcao()

    match opcao:
        case 1:
            limpar()
            tarefa = input("Digite a tarefa: ")
            adicionartarefa=ControllerAdicionarTarefa(tarefa)
            parar()

        case 2:
            limpar()
            print("--| Lista de Tarefas |--")
            listarTarefa=ControllerListarTarefa()
            excluir = (input("\nDigite o número da tarefa que deseja excluir: "))
            excluirTarefa=ControllerExcluirTarefa(excluir)
            print("--| Nova Lista de Tarefas |--")
            listarTarefa=ControllerListarTarefa()
            parar()
        case 3:
            limpar()
            print("--| Lista de Tarefas |--")
            listarTarefa=ControllerListarTarefa()
            parar()

            
        case 00:
            sair=False
        case _:
            limpar()
            print("Opção inválida")
            parar()

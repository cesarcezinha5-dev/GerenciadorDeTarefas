print("**Seja bem-vindo ao Gerenciador de Tarefas**\n")
def menu():
    print("1-Adicionar tarefa")
    print("2-Listar tarefas")
    print("3-Remover tarefa")
    print("4-Sair")
tarefas = []


while True:
    menu()
    opcao=input("\nEscolha uma das opções acima: ")

    if opcao == "1":
        nova_tarefa=input("Digite a tarefa: ")
        tarefas.append(nova_tarefa)
    
    elif opcao == "2":
        for t in tarefas:
            print(t)
                
    elif opcao == "3":
        tarefa_remover=input("Digite o nome da tarefa que deseja remover da lista: ")
        if tarefa_remover in tarefas:
            tarefas.remove(tarefa_remover)
            print("Tarefa removida!")
        else:
            print("Tarefa nao encontrada na lista")

    elif opcao == "4":
        print("Saindo...")
        break




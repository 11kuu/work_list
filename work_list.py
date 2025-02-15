
lista_tarefas = []
lista_tarefas_concluidas = []

def adicionar_tarefa():
    tarefa = input("\nDigite uma nova tarefa: ")
    lista_tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def remover_tarefa():
    if not lista_tarefas:
        print("\nNenhuma tarefa para remover!")
        return

    print("\nTarefas pendentes:")
    for i, tarefa in enumerate(lista_tarefas):
        print(f"{i + 1}. {tarefa}")

    try:
        indice = int(input("\nDigite o número da tarefa que concluiu: ")) - 1
        if 0 <= indice < len(lista_tarefas):
            tarefa_concluida = lista_tarefas.pop(indice)
            lista_tarefas_concluidas.append(tarefa_concluida)
            print(f"Tarefa '{tarefa_concluida}' marcada como concluída!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Entrada inválida! Digite um número.")

def exibir_tarefas():
    if not lista_tarefas:
        print("\nNenhuma tarefa pendente!")
    else:
        print("\nTarefas pendentes:")
        for i, tarefa in enumerate(lista_tarefas):
            print(f"{i + 1}. {tarefa}")

    if lista_tarefas_concluidas:
        print("\nTarefas concluídas:")
        for tarefa in lista_tarefas_concluidas:
            print(f"- {tarefa}")

def menu():
    while True:
        print("\n===== LISTA DE TAREFAS =====")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa (marcar como concluída)")
        print("3. Exibir Tarefas")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            remover_tarefa()
        elif opcao == "3":
            exibir_tarefas()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")


menu()

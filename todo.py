tarefas = []

def adicionar_tarefa():
    nome_tarefa = input("Nome da tarefa: ")
    data_vencimento = input("Digite a data de vencimento (opcional):")

    tarefa = {
        "nome": nome_tarefa,
        "concluida": False
    }

    if data_vencimento:
        tarefa["data_vencimento"] = data_vencimento

    tarefas.append(tarefa)

    print(f'Tarefa {nome_tarefa} adicionada à lista')

def remover_tarefa():
    nome_tarefa = input("Digite o nome da tarefa que deseja remover: ")

    tarefa_encontrada = None
    for tarefa in tarefas:
        if tarefa["nome"] == nome_tarefa:
            tarefa_encontrada = tarefa
            break

    if tarefa_encontrada:
        tarefas.remove(tarefa_encontrada)
        print(f'Tarefa {nome_tarefa} removida da lista.')
    else:
        print(f'Tarefa {nome_tarefa} não encontrada na lista')

def listar_tarefas():
    print("Tarefas pendentes:")

    for i, tarefa in enumerate(tarefas):
        if not tarefa['concluida']:
            nome = tarefa["nome"]
            data_vencimento = tarefa.get("data_vencimento", "N/A")
            print(f'{i + 1}. {nome} (Data de Vencimento: {data_vencimento})')

def marcar_como_concluida():
    nome_tarefa = input("Digite o nome da tarefa que deseja marcar como concluida: ")

    for tarefa in tarefas:
        if tarefa["nome"] == nome_tarefa:
            if not tarefa["concluida"]:
                tarefa['concluida'] = True
                print(f'Tarefa {nome_tarefa} marcada como concluída.')
            else:
                print(f'Tarefa {nome_tarefa} já está marcada como concluida')
            return 
        
    print(f'Tarefa {nome_tarefa} não encontrada na lista')


while True:

    print("=== Lista de Tarefas ====")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Listar Tarefa")
    print("4. Marcar como Concluída")
    print("5. Sair")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        adicionar_tarefa()

    elif escolha == 2:
        remover_tarefa()

    elif escolha == 3:
        listar_tarefas()

    elif escolha == 4:
        marcar_como_concluida()

    else:
        exit()
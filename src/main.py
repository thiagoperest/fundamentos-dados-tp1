from datetime import date


tasks = [
    {
        "id": 1,
        "description": "Estudar Python",
        "created_at": date(2026, 4, 1),
        "status": "pendente",
        "deadline": date(2026, 4, 30),
        "urgency": "alta",
    },
    {
        "id": 2,
        "description": "Aprender inglês",
        "created_at": date(2026, 4, 5),
        "status": "pendente",
        "deadline": date(2026, 12, 31),
        "urgency": "normal",
    },
    {
        "id": 3,
        "description": "Assistir workshops sobre arquitetura de software",
        "created_at": date(2026, 4, 10),
        "status": "pendente",
        "deadline": date(2026, 5, 31),
        "urgency": "normal",
    },
]


def add_task(description, deadline=None, urgency="normal"):
    """
    Adiciona uma nova tarefa à lista de tarefas pendentes.

    Args:
        description (str): Descrição da tarefa.
        deadline (date, optional): Prazo final da tarefa. Padrão: None.
        urgency (str, optional): Nível de urgência da tarefa ("baixa", "normal", "alta"). Padrão: "normal".

    """
    next_id = max(task["id"] for task in tasks) + 1 if tasks else 1
    task = {
        "id": next_id,
        "description": description,
        "created_at": date.today(),
        "status": "pendente",
        "deadline": deadline,
        "urgency": urgency,
    }
    tasks.append(task)
    print(f"\nTarefa #{task['id']} adicionada com sucesso.")
    return task


def list_tasks(tasks_list=None):
    """
    Lista todas as tarefas pendentes, enumerando-as.

    Args:
        tasks_list (list, optional): Lista de tarefas a exibir. Padrão: lista total de tasks.

    Returns:
        int: Quantidade de tarefas pendentes exibidas.
    """
    if tasks_list is None:
        tasks_list = tasks

    pending = [task for task in tasks_list if task["status"] == "pendente"]

    if not pending:
        print("\nNenhuma tarefa pendente encontrada.")
        return 0

    print("\n=== Tarefas Pendentes ===")
    for i, task in enumerate(pending, start=1):
        deadline_str = task["deadline"].strftime("%d/%m/%Y") if task["deadline"] else "Sem prazo"
        print(f"\n{i}. [ID #{task['id']}] {task['description']}")
        print(f"   Criado em : {task['created_at'].strftime('%d/%m/%Y')}")
        print(f"   Prazo     : {deadline_str}")
        print(f"   Urgência  : {task['urgency']}")
        print(f"   Status    : {task['status']}")

    return len(pending)


def complete_task(task_id, status="concluída"):
    """
    Marca uma tarefa específica como concluída.

    Args:
        task_id (int): ID da tarefa a ser marcada como concluída.
        status (str, optional): Status a ser atribuído à tarefa. Padrão: "concluída".

    Returns:
        dict | None: A tarefa atualizada, ou None se não encontrada.
    """
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            print(f"\nTarefa #{task_id} marcada como '{status}' com sucesso.")
            return task
    print(f"\nTarefa #{task_id} não encontrada.")
    return None


def main():
    while True:
        print("\n=== Sistema de Gestão de Tarefas ===")
        print("1 - Adicionar Tarefa")
        print("2 - Listar Tarefas")
        print("3 - Marcar Tarefa como Concluída")
        print("0 - Sair")

        option = input("\nEscolha uma opção: ").strip()

        if option == "1":
            description = ""
            while not description:
                description = input("Descrição da tarefa (obrigatório): ").strip()
                if not description:
                    print("A descrição não pode ser vazia.")
            deadline = None
            while not deadline:
                deadline_input = input("Prazo final (DD/MM/AAAA) (obrigatório): ").strip()
                if not deadline_input:
                    print("O prazo final não pode ser vazio.")
                else:
                    try:
                        day, month, year = deadline_input.split("/")
                        parsed = date(int(year), int(month), int(day))
                        if parsed < date.today():
                            print("O prazo final não pode ser uma data anterior a hoje!")
                        else:
                            deadline = parsed
                    except (ValueError, TypeError):
                        print("Formato inválido. Use DD/MM/AAAA (ex: 30/04/2026).")
            urgency = input("Urgência (baixa/normal/alta) [padrão: normal]: ").strip() or "normal"

            add_task(description, deadline=deadline, urgency=urgency)

        elif option == "2":
            list_tasks()

        elif option == "3":
            list_tasks()
            pending = [task for task in tasks if task["status"] == "pendente"]
            if pending:
                task_id = None
                while task_id is None:
                    try:
                        task_id = int(input("\nDigite o ID da tarefa a concluir: ").strip())
                    except ValueError:
                        print("ID inválido. Digite um número.")
                        task_id = None
                complete_task(task_id)

        elif option == "0":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

# Python - INFNET - TP1

![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Ativo-success.svg)

Sistema de gestão de tarefas desenvolvido como projeto prático com Python, implementando operações de adição, listagem, conclusão e remoção de tarefas via interface de linha de comando, utilizando loops, manipulação de listas e funções documentadas com DocStrings.

## Sobre o Projeto

Este projeto foi desenvolvido como parte do **TP1: Fundamentos de Dados** do Instituto Infnet, implementando um sistema completo de gestão de tarefas via CLI com manipulação de listas, funções com parâmetros por palavra-chave, parâmetros padrão e retorno de valores.

**Instituto Infnet** - Projeto de Bloco  
**Disciplina:** Fundamentos de Dados
**Aluno:** Thiago Teodoro Peres

## Arquitetura

A aplicação implementa uma arquitetura simples baseada em funções com separação clara de responsabilidades:

```
Interface (main — loop while + menu de opções)
        ↓
Funções de Negócio (add_task / list_tasks / complete_task / remove_task)
        ↓
Estrutura de Dados (lista tasks — list[dict])
```

Cada tarefa é representada como um dicionário com os seguintes metadados:

```python
{
    "id":          int,   # Identificador único incremental
    "description": str,   # Descrição da tarefa
    "created_at":  date,  # Data de criação
    "status":      str,   # "pendente" | "concluída"
    "deadline":    date,  # Prazo final
    "urgency":     str,   # "baixa" | "normal" | "alta"
}
```

## Funcionalidades Implementadas

- **Adicionar Tarefa** — Permite ao usuário adicionar uma nova tarefa à lista com validação de campos obrigatórios e prazo
- **Listar Tarefas** — Exibe todas as tarefas pendentes enumeradas com seus dados de forma completa
- **Marcar como Concluída** — Permite ao usuário marcar uma tarefa específica como concluída pelo ID
- **Remover Tarefa** — Permite ao usuário remover permanentemente uma tarefa da lista pelo ID

## Como Executar

### Pré-requisitos

- Python 3.10 ou superior

### Execução

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/thiagoperest/fundamentos-dados-tp1.git
   cd fundamentos-dados-tp1
   ```

2. **Execute o programa:**
   ```bash
   python src/main.py
   ```

### Menu de opções

```
=== Sistema de Gestão de Tarefas ===
1 - Adicionar Tarefa
2 - Listar Tarefas
3 - Marcar Tarefa como Concluída
4 - Remover Tarefa
0 - Sair
```

## Estrutura do Projeto

```
fundamentos-dados-tp1/
├── src/
│   └── main.py
└── .gitignore
```

## Funções Implementadas

| Função | Parâmetros | Retorno | Descrição |
|---|---|---|---|
| `add_task` | `description`, `deadline=None`, `urgency="normal"` | `dict` | Adiciona nova tarefa à lista |
| `list_tasks` | `tasks_list=None` | `int` | Lista tarefas pendentes enumeradas |
| `complete_task` | `task_id`, `status="concluída"` | `dict \| None` | Marca tarefa como concluída |
| `remove_task` | `task_id` | `dict \| None` | Remove tarefa da lista |

## Tecnologias Utilizadas

- **Python 3.10+** — Linguagem principal
- **datetime** — Manipulação de datas (data de criação e prazo final)

## Contato

**Thiago Teodoro Peres**  
Email: thiago.peres@al.infnet.edu.br  
Instituto Infnet - Fundamentos de Dados com Python

---

**Projeto desenvolvido para o Instituto Infnet - TP1**

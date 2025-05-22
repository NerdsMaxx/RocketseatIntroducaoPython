from operator import truediv
from typing import TypeAlias

Tarefa: TypeAlias = dict[str, str | bool]

def tela_inicial():
    tarefas: list[Tarefa] = []
    opcao: int = 0

    while opcao != 6:
        print("\nMenu do Gerenciador de Lista de tarefas:")
        print("1. Adicionar tarefa")
        print("2. Ver tarefas")
        print("3. Atualizar tarefa")
        print("4. Completar tarefa")
        print("5. Deletar tarefas completadas")
        print("6. Sair")
        opcao = int(input("Digite a sua escolha: "))

        match opcao:

            case 1:
                adicionar_tarefa(tarefas, input("Digite o nome da tarefa: "))

            case 2:
                if validar_lista(tarefas):
                    listar_tarefas(tarefas)

            case 3:
                if validar_lista(tarefas):
                    listar_tarefas(tarefas)
                    indice_str: str = input("\nDigite qual tarefa deseja atualizar: ")
                    if validar_int(indice_str):
                        indice: int = int(indice_str)
                        novo_nome_tarefa: str = input("Digite a nova tarefa: ")
                        atualizar_nome_tarefa(tarefas, indice, novo_nome_tarefa)

            case 4:
                if validar_lista(tarefas):
                    listar_tarefas(tarefas)
                    indice_str: str = input("\nDigite qual tarefa deseja completar: ")
                    if validar_int(indice_str):
                        indice: int = int(indice_str)
                        completar_tarefa(tarefas, indice)

            case 5:
                if validar_lista(tarefas):
                    deletar_tarefas_completadas(tarefas)
                    if len(tarefas) > 0:
                        listar_tarefas(tarefas)



def adicionar_tarefa(tarefas: list[Tarefa], nome_tarefa: str):
    if len(nome_tarefa.strip()) == 0:
        print("\nErro: É obrigatório digitar a tarefa.")
        return
   
    tarefas.append({"nome": nome_tarefa, "completada": False})
    print(f"\nTarefa \"{nome_tarefa}\" foi adicionada com sucesso!")
    
def listar_tarefas(tarefas: list[Tarefa]):
    print("\nLista de tarefas")
    for i, t in enumerate(tarefas, start=1):
        status = "[✓]" if t["completada"] == True else "[]"
        print(f"{i}. {status} {t["nome"]}")

def atualizar_nome_tarefa(tarefas: list[Tarefa], indice: int, novo_nome_tarefa: str):
    if validar_indice(tarefas, indice):
        tarefas[indice - 1]["nome"] = novo_nome_tarefa
        print(f"\nTarefa {indice} atualizada para \"{novo_nome_tarefa}\"!")

def completar_tarefa(tarefas: list[Tarefa], indice: int):
    if validar_indice(tarefas, indice):
        tarefas[indice - 1]["completada"] = True
        print(f"\nTarefa {indice} marcada como completada!")

def deletar_tarefas_completadas(tarefas: list[Tarefa]):
    for t in tarefas:
        if t["completada"] == True:
            tarefas.remove(t)

    print("\nTarefas completadas deletadas com sucesso!")


def validar_indice(tarefas: list[Tarefa], indice: int) -> bool:
    tamanho: int = len(tarefas)
    if tamanho != 0 and (indice <= 0 or indice > tamanho):
        print(f"\nIndice {indice} inválido. A lista tem tamanho {tamanho}.")
        return False
    return True

def validar_lista(tarefas: list[Tarefa]):
    if len(tarefas) == 0:
        print("\nNão há tarefas!")
        return False
    return True

def validar_int(valor: str):
    if not valor.isdigit():
        print("\nNão pode ser texto, tem que ser um número!")
        return False
    return True

tela_inicial()

print("\nPrograma finalizado")
import json

tarefas = []

def menu_principal():
    while True:
        print("\n Menu Principal")
        print("1 - Adicionar Tarefa")
        print("2 - Listar Tarefa")
        print("3 - Marcar como Concluída")
        print("4 - Remover Tarefa")
        print("5 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
                print("❌ Digite um número Válido! ")
                continue
        
        if opcao == 1:
            adicionar_tarefa()
        elif opcao == 2:
            listar_tarefa()
        elif opcao == 3:
            marcar_tarefa()
        elif opcao == 4:
             remover_tarefa()
        elif opcao == 5:
             print("Saindo...")
             break
        else:
            print("❌ Opção inválida! Tente novamente.")

        
def adicionar_tarefa():
     add_tarefa = input("Digite um título para sua tarefa: ")
     nova_tarefa = {"titulo": add_tarefa, "status":False}
     tarefas.append(nova_tarefa)
     salvar_tarefas()
     print("Tarefa adicionada com sucesso.")

def listar_tarefa():
     for i, tarefa in enumerate(tarefas):
        status = "✅" if tarefa["status"] else "❌"
        print(f"{i} - [{status}] {tarefa['titulo']}")

def marcar_tarefa():
     listar_tarefa()
     try:
          indice = int(input("Digita o número da tarefas para que seja concluída"))
          if 0 <= indice < len(tarefas):
               tarefas[indice]["status"] = True
               print(f"✅ Tarefa marcada como concluída!")
               salvar_tarefas()
          else:
               print("❌ Índice inválido.")
     except ValueError:
          print("❌ Por favor, digite um número válido.")
          

def remover_tarefa():
     listar_tarefa()
     try:
        indice = int(input("Digite o número da tarefa que deseja remover:"))
        if 0 <= indice < len(tarefas):
             tarefas.pop(indice)
             salvar_tarefas()
        else:
             print("❌ Índice inválido.")
     except ValueError:
          print("❌ 🗑️ Tarefa removida com sucesso!.")


def salvar_tarefas():
     with open("tarefas.json", "w", encoding="utf-8") as arquivo:json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

tarefas = carregar_tarefas ();
menu_principal()
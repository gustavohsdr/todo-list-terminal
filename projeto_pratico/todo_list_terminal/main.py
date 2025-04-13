import json
import uuid
from datetime import datetime
tarefas = []

def menu_principal():
    while True:
        print("\n Menu Principal")
        print("1 - Adicionar Tarefa")
        print("2 - Listar Tarefa")
        print("3 - Marcar como Concluída")
        print("4 - Remover Tarefa")
        print("5 - Listar e Ordenar")
        print("6 - Histórico de Log")        
        print("7 - Sair")

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
             listar_tarefa_ordenada()
        elif opcao == 6:
             listar_log()
        elif opcao == 7:
             print("Saindo...")
             break
        else:
            print("❌ Opção inválida! Tente novamente.")

def salvar_tarefas():
     with open("tarefas.json", "w", encoding="utf-8") as arquivo:
          json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    
def registrar_log(acao, titulo):
     log = {
          "id": str(uuid.uuid4()),
          "acao":acao,
          "titulo":titulo,
          "data":datetime.now().strftime("%Y-%m-%d %H:%M:%S",)
          }
     try:
          with open ("historico.json", "r", encoding="utf-8") as arquivo:
               historico = json.load(arquivo)
     except FileNotFoundError:
          historico = []
     historico.append(log)

     with open("historico.json", "w", encoding="utf-8") as arquivo:
          json.dump(historico, arquivo, ensure_ascii=False, indent=4)

def registrar_erro(mensagem, tipo="erro"):
     error_log = {
          "id": str(uuid.uuid4()),
          "tipo": tipo,
          "mensagem": mensagem,
          "data":datetime.now().strftime("%Y-%m-%d %H:%M:%S",)
     }
     try:
          with open ("erros.json", "r", encoding="utf-8") as arquivo:
               erros = json.load(arquivo)
     except FileNotFoundError:
          erros = []
     erros.append(error_log)

     with open("erros.json", "w", encoding="utf-8") as arquivo:
          json.dump(erros, arquivo, ensure_ascii=False, indent=4)
        
def adicionar_tarefa():
     add_tarefa = input("Digite um título para sua tarefa: ")
     data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M")
     nova_tarefa = {"titulo": add_tarefa, "status":False, "data": data_criacao,}
     tarefas.append(nova_tarefa)
     salvar_tarefas()
     registrar_log("Adicionada", add_tarefa)
     print("Tarefa adicionada com sucesso.")

def listar_tarefa():
     for i, tarefa in enumerate(tarefas):
        status = "✅" if tarefa["status"] else "❌"
        print(f"{i} - [{status}] {tarefa['titulo']}")

def listar_log():
     try:
          with open("historico.json", "r", encoding="utf-8") as arquivo:
               historico = json.load(arquivo)
               for i, entrada in enumerate (historico):
                    print(f"{i} - [{entrada['data']}] {entrada['acao']}: {entrada['titulo']}")
     except FileNotFoundError:
          print("⚠️ Nenhum Histórico Encontrado")


def marcar_tarefa():
     listar_tarefa()
     entrada = input("Digita o número da tarefas para que seja concluída: ")
     try:
          indice = int(entrada)
          if 0 <= indice < len(tarefas):
               tarefas[indice]["status"] = True
               print(f"✅ Tarefa marcada como concluída!")
               salvar_tarefas()
               registrar_log("Concluída", tarefas[indice]["titulo"])
          else:
               registrar_erro(f"Erro: índice fora do intervalo. Usuário informou: [{indice}]", tipo="indice_invalido")
               print("❌ Índice inválido.")
     except ValueError:
          registrar_erro(f"Erro: valor inválido digitado. Usuário informou: [{entrada}]", tipo="valor_invalido")
          print("❌ Por favor, digite um número válido.")
          

def remover_tarefa():
     listar_tarefa()
     entrada = input("Digite o número da tarefa que deseja remover: ")
     try:
        indice_remover = int(entrada)
        if 0 <= indice_remover < len(tarefas):
             registrar_log("Removida", tarefas[indice_remover]["titulo"])
             tarefas.pop(indice_remover)
             salvar_tarefas()
             print("❌ 🗑️ Tarefa removida com sucesso!.")
        else:
             registrar_erro(f"Erro: índice fora do intervalo. Usuário informou: [{indice_remover}]", tipo="indice_invalido")
             print("❌ Índice inválido.")
     except ValueError:
          registrar_erro(f"Erro: valor inválido digitado. Usuário informou: [{entrada}]", tipo="valor_invalido")
          print("❌ Por favor, digite um número válido.")

def listar_tarefa_ordenada ():
     tarefas_ordenadas = sorted(tarefas, key=lambda tarefa: tarefa['titulo'].lower())
     for i, tarefa in enumerate(tarefas_ordenadas):
          status = "✅" if tarefa["status"] else "❌"
          print(f"{i} - [{status}] {tarefa['titulo']} ({tarefa['data']})")

tarefas = carregar_tarefas ();
menu_principal()
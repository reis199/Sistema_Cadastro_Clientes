import json

import csv

clientes = []

def salvar_clientes():
    with open("clientes.json","w", encoding="utf-8") as arquivo:
        json.dump(clientes, arquivo, ensure_ascii=False, indent=4)

def carregar_clientes():
    try:
        with open("clientes.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

clientes = carregar_clientes()

import os

print("Arquivo JSON:", os.path.abspath("clientes.json"))
print("Clientes carregados:", clientes) 

def mostrar_menu():
    print("\n=== CADASTRO DE CLIENTES V6 ===")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Pesquisar cliente")
    print("4 - Editar cliente")
    print("5 - Excluir cliente")
    print("6 - Sair")
    print("7 - Total de clientes")
    print("8 - Relatorio de clientes")
    print("9 - Exportar clientes para CSV")
    print("10 - Importar clientes de CSV")


mostrar_menu()

def validar_telefone(telefone):
    return telefone.isdigit() and len(telefone) in (10, 11)


def cadastrar_cliente():
    print("\n=== CADASTRAR CLIENTE ===")

    nome = input("digite o nome do cliente: ").strip()

    while nome == "":
        print("Erro! O  nome nao pode ficar vazio.")
        nome = input("digite o nome do cliente: ").strip()

    telefone = input("Digite o telefone: ").strip()

    while not validar_telefone(telefone):
        print("erro! digite um telefone com 10 ou 11 números.")
        telefone = input("digite o telefone: ").strip()

    for cliente_existente in clientes:
         if cliente_existente["telefone"] == telefone:
            print("Erro! Este telefone já está cadastrado.")
            return

         for cliente_existente in clientes:
             if cliente_existente["nome"].strip().lower() == nome.lower():
                print("Erro! Este nome já está cadastrado.")
                return

    cliente = {
        "nome": nome,
        "telefone": telefone
    }

    clientes.append(cliente)

    salvar_clientes()

    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    print("\n=== CLIENTES CADASTRADOS ===")

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in clientes:
        print("Nome:", cliente["nome"])
        print("Telefone:", cliente["telefone"])
        print("--------------------")
    
def contar_clientes():
    total = len(clientes)

    print("\n=== TOTAL DE CLIENTES ===")
    print(f"clientes cadastrados:{total}")

    print("\n=== CLIENTES CADASTRADOS ===")

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in clientes:
            print("Nome:", cliente["nome"])
            print("Telefone:", cliente["telefone"])
            print("--------------------")

def relatorio_clientes():
    print("\n=== RELATÓRIO DE CLIENTES ===")

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    clientes_ordenados = sorted(
        clientes,
        key=lambda cliente: cliente["nome"].lower()
    )

    for numero, cliente in enumerate(clientes_ordenados, start=1):
        print(f"\nCliente {numero}")
        print("Nome:", cliente["nome"])
        print("Telefone:", cliente["telefone"])
        print("--------------------")

    print(f"\nTotal de clientes: {len(clientes_ordenados)}")



def exportar_clientes():

    print("\n=== EXPORTAR CLIENTES PARA CSV ===")

    if not clientes:
        print("nenhum cliente para exportar.")
        return

    with open("clientes.csv", "w", newline="", encoding="utf-8-sig") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")

        escritor.writerow(["nome", "telefone"])

        for cliente in clientes:
            escritor.writerow([cliente["nome"], cliente["telefone"]])

    print("clientes exportados com sucesso!")

def importar_clientes():
    print("\n=== iIMPORTAR CLIENTES DE CSV ===")    

    try:
        with open("clientes.csv", "r", encoding="utf-8-sig") as arquivo:
            leitor = csv.DictReader(arquivo, delimiter=";")
            importados = 0

            for linha in leitor:
                 nome = linha["nome"].strip()
                 telefone = linha["telefone"].strip()

                 if not nome:
                     print("cliente ignorado: nome vazio.")
                     continue
                 if not validar_telefone(telefone):
                     print(f"cliente ignorado: telefone inválido ({telefone}).")
                     continue

                 duplicado = False

                 for cliente in clientes:
                    if (cliente["nome"].strip().lower() == nome.lower()
                            or cliente["telefone"] == telefone):
                        duplicado = True
                        break
                 if not duplicado:
                        clientes.append({
                            "nome": nome,
                            "telefone": telefone
                        })
                        importados += 1
        if importados > 0:
            salvar_clientes()

        print(f"clientes importados com sucesso: {importados}")     
    except  FileNotFoundError:
        print("erro! Arquivo clientes.csv não encontrado.")        

def pesquisar_cliente():      

    print("\n=== PESQUISAR CLIENTE ===")

    busca = input("Digite o nome  ou telefone do cliente: ").strip().lower()
    encontrado = False

    for cliente in clientes:
        if busca == cliente["nome"].strip().lower() or busca == cliente["telefone"]:
            print("Nome:", cliente["nome"])
            print("Telefone:", cliente["telefone"])
            encontrado = True

    if not encontrado:
        print("Cliente não encontrado!")

def editar_cliente():
    print("\n=== EDITAR CLIENTE ===")

    busca = input("Digite o nome do cliente que deseja editar: ").strip().lower()

    for cliente in clientes:
        if busca == cliente["nome"].strip().lower():
            print("Cliente encontrado!")
            print("Nome atual:", cliente["nome"])
            print("Telefone atual:", cliente["telefone"])

            novo_nome = input("digite o novo nome: ").strip()
            while novo_nome == "":
                print("Erro! O nome não pode ficar vazio.")
                novo_nome = input("Digite o novo nome: ").strip()
            novo_telefone = input("digite o novo telefone: ").strip()
            while not validar_telefone(novo_telefone):
                print("Erro! Digite um telefone com 10 ou 11 números.")
                novo_telefone = input("Digite o novo telefone: ").strip()

            for cliente_existente in clientes:
                 if cliente_existente is not cliente:
                   if cliente_existente["telefone"] == novo_telefone:
                       print("Erro! Este telefone pertence a outro cliente.")
                       return

            for cliente_existente in clientes:
                 if cliente_existente is not cliente:
                  if cliente_existente["nome"].strip().lower() == novo_nome.lower():
                     print("Erro! Este nome pertence a outro cliente.")
                     return

            cliente["nome"] = novo_nome
            cliente["telefone"] = novo_telefone

            salvar_clientes()
            

            print("Cliente atualizado com sucesso!")
            return

    print("Cliente não encontrado!")


def excluir_cliente():
    print("\n=== EXCLUIR CLIENTE ===")

    busca = input("Digite o nome do cliente que deseja excluir: ").strip().lower()

    for cliente in clientes:
        if busca == cliente["nome"].strip().lower():
                        print("Cliente encontrado:", cliente["nome"])

                        confirmar = input("Deseja realmente excluir? (s/n): ").strip().lower()

                        while confirmar not in ("s", "n"):
                            print("Erro! Digite apenas s ou n.")
                            confirmar = input("Deseja realmente excluir? (s/n): ").strip().lower()

                        if confirmar == "s":
                            clientes.remove(cliente)
                            salvar_clientes()
                            
                            print("Cliente excluído com sucesso!")
                        else:
                            print("Exclusão cancelada!")

                        return

    print("Cliente não encontrado!") 
while True:
    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()

    elif opcao == "2":
        listar_clientes()

    elif opcao == "3":
        pesquisar_cliente()

    elif opcao == "4":
       editar_cliente()

    elif opcao == "5":
        excluir_cliente()

    elif opcao == "6":
        print("Encerrando o sistema...")
        break

    elif opcao == "7":
        contar_clientes()

    elif opcao == "8":
        relatorio_clientes()

    elif opcao == "9":
        exportar_clientes()

    elif opcao == "10":
        importar_clientes()

    else:
        print("Opção inválida!")


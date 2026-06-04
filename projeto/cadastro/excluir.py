import json

ARQUIVO = "data/clientes.json"

def excluir_cliente():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
          clientes = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("ERRO: Arquivo de clientes não encontrado ou inválido.")
        return

    while True:
        cpf = input("Digite o CPF (11 dígitos): ").strip()
        if cpf.isdigit() and len(cpf) == 11:
            break
        print("ERRO: CPF deve conter exatamente 11 números.")

    cliente_encontrado = None
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            cliente_encontrado = cliente
            break

    if cliente_encontrado is None:
        print("CLIENTE NÃO ENCONTRADO.")
        return

    print("\nCLIENTE ENCONTRADO")
    print(f"Nome: {cliente_encontrado['nome']}")
    print(f"CPF: {cliente_encontrado['cpf']}")
    print(f"Dependentes: {len(cliente_encontrado['dependentes'])}")

    while True:
        opcao = input("Deseja excluir este cliente e dependentes? (S/N): ").upper()
        if opcao in ["S", "N"]:
            break
        print("ERRO: Digite apenas S ou N.")

    if opcao == "S":
        clientes.remove(cliente_encontrado)
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump(clientes, arquivo, indent=4, ensure_ascii=False)
        print("CLIENTE REMOVIDO COM SUCESSO.")
    else:
        print("EXCLUSÃO CANCELADA.")



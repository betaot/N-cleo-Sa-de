import json
import os

ARQUIVO = "data/clientes.json"

def carregar_dados():

    if not os.path.exists(ARQUIVO):
        return []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)

    except json.JSONDecodeError:
        return []


def salvar_dados(novo_cliente):

    dados = carregar_dados()

    dados.append(novo_cliente)

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
def cpf_existe(cpf):
    clientes = carregar_dados()

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return True
    return False
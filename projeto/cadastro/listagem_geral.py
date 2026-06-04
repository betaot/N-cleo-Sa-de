import json

def listar_clientes():

    try:

        with open("data/clientes.json", "r", encoding="utf-8") as arquivo:

            clientes = json.load(arquivo)

        if len(clientes) == 0:

            print("\nNenhum cliente cadastrado.")

            input("\nPressione ENTER para voltar...")

            return

        print("\n========== LISTAGEM GERAL ==========\n")

        for cliente in clientes:

            print(f"CPF: {cliente['cpf']}")

            print(f"Nome: {cliente['nome']}")

            print(f"Sexo: {cliente['sexo']}")

            print(f"Telefone: {cliente['telefone']}")

            print(f"Email: {cliente['email']}")

            print(f"Idade: {cliente['idade']}")

            if cliente.get("dependentes"):

                print("Dependentes:")

                for dep in cliente["dependentes"]:

                    print(f" CPF: {dep['cpf']}")

                    print(f" Nome: {dep['nome']}")

                    print(

                        f" Idade/Nascimento: {dep.get('idade', dep.get('nascimento', 'Não informado'))}"

                    )

            else:

                print("Dependentes: Nenhum")

            print(f"Plano: {cliente['plano']}")

            print(f"Valor do Plano: R$ {cliente['valor_plano']}")

            print(f"Vencimento: {cliente['vencimento']}")

            print("-" * 50)

        input("\nPressione ENTER para voltar...")

    except FileNotFoundError:

        print("Erro: arquivo clientes.json não encontrado.")

    except json.JSONDecodeError:

        print("Erro: o arquivo JSON está inválido.")
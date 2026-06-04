import json

def editar_cliente():

    while True:
        with open("data/clientes.json", "r", encoding="utf-8") as arquivo:
            clientes = json.load(arquivo)

        novo_dado = 0

        cpf_procurado = input(
            "digite seu usuario que deseja modificar ou 0 para sair: "
        )

        if cpf_procurado == "0":
            break

        cpf_existente = False

        for cliente_ in clientes:
            if cpf_procurado == cliente_["cpf"]:
                cpf_existente = True

                while True:
                    try:
                        novo_dado = int(input(
                            "que dado voce quer mudar digite\n"
                            "1: cpf      2: nome\n"
                            "3: sexo     4: email\n"
                            "5: idade    6: titular\n"
                            "7: telefone 8: dependentes\n"
                            "9: plano    10: sair\n"
                        ))

                        if novo_dado < 1 or novo_dado > 10:
                            print("digite um valor entre 1 e 10")
                        else:
                            break

                    except ValueError:
                        print("digite um valor valido")

                if novo_dado == 1:
                    cpf_novo = input("digite o novo cpf: ")
                    cliente_["cpf"] = cpf_novo

                elif novo_dado == 2:
                    nome_novo = input("digite o novo nome: ")
                    cliente_["nome"] = nome_novo

                elif novo_dado == 3:
                    novo_sexo = input("digite o sexo: ")
                    cliente_["sexo"] = novo_sexo

                elif novo_dado == 4:
                    novo_email = input("digite o novo email: ")
                    cliente_["email"] = novo_email

                elif novo_dado == 5:
                    while True:
                        try:
                            nova_idade = int(input("digite a nova idade: "))
                            cliente_["idade"] = nova_idade
                            break
                        except ValueError:
                            print("digite um valor valido")

                elif novo_dado == 6:
                    novo_titular = input("digite o novo titular: ")
                    cliente_["titular"] = novo_titular

                elif novo_dado == 7:
                    novo_telefone = input("digite o novo numero de telefone: ")
                    cliente_["telefone"] = novo_telefone

                elif novo_dado == 8:
                    nome = input("Nome do dependente: ")

                    while True:
                        try:
                            idade = int(input("Idade do dependente: "))
                            break
                        except ValueError:
                            print("digite um numero valido")

                    sexo = input("Sexo do dependente: ")

                    novo_dependente = {
                        "nome": nome,
                        "idade": idade,
                        "sexo": sexo
                    }

                    cliente_["dependentes"].append(novo_dependente)

                elif novo_dado == 9:
                    novo_plano = input("digite o novo plano: ")
                    cliente_["plano"] = novo_plano

                elif novo_dado == 10:
                    break

                if novo_dado != 10:
                    with open(
                        "data/clientes.json",
                        "w",
                        encoding="utf-8"
                    ) as arquivo:
                        json.dump(
                            clientes,
                            arquivo,
                            indent=4,
                            ensure_ascii=False
                        )

                    print("Dados atualizados com sucesso!")

                break

        if novo_dado == 10:
            break

        if not cpf_existente:
            print("cpf nao encontrado")
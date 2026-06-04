from others.utilidades import limpar_tela, calcular_idade
from armazenamento.armazenamento import salvar_dados, cpf_existe
from cadastro.calculo_plano import calculo
from datetime import datetime

def fazer_cadastro():
    limpar_tela()#Função para limpar o Terminal após uma ação
    print("Bem vindo ao Cadastro, siga as instruções abaixo!")
    while True:
        cpf = input("Digite o seu CPF: ").strip()#CPF do cliente
        if not (cpf.isdigit() and len(cpf) == 11):#Verificação para validar o cpf
            print("CPF inválido! Deve conter 11 números.")
        elif cpf_existe(cpf):
            print("Esse cpf já existe!")
        else:
            break

    limpar_tela()
    nome = input("Digite o seu nome completo: ").strip()#Nome do Cliente

    while not all(parte.isalpha() for parte in nome.split()):#Verificação para validar o nome
        print("Digite apenas letras!")
        nome = input("Digite o nome completo: ").strip()
    limpar_tela()

    while True:
        sexo = input("Digite 1 para masculino, Digite 2 para feminino: ")#Sexo do cliente

        if sexo == "1":
            sexo = "masculino"
            break
        elif sexo == "2":
            sexo = "feminino"
            break
        else:
            print("Opção inválida!")

    limpar_tela()

    email = input("Digite o seu email: ").strip().lower()#Email do cliente
    while "@gmail.com" not in email and "@hotmail.com" not in email and "@outlook" not in email:#Verificação para validar email
        print("Email inválido!")
        email = input("Digite o email: ").strip().lower()
    limpar_tela()
    while True:
        data_nascimento = input(
            "Digite sua data de nascimento (dd/mm/aaaa): ").strip()

        try:
            datetime.strptime(data_nascimento, "%d/%m/%Y")
            idade = calcular_idade(data_nascimento)
            break

        except ValueError:
            print("Data inválida!")

    limpar_tela()

    titular = input("Digite o titular: ").strip()#titular do cliente
    limpar_tela()

    telefone = input("Digite seu número de telefone: ").strip()#Telefone do CLiente
    while not telefone.isdigit():#Verificação para validar o telefone
        print("Digite apenas números!")
        telefone = input("Digite seu número de telefone: ").strip()
    limpar_tela()

    dependentes = []#Lista onde irá ficar os dependentes do cliente

    while True:
        p_dependente = input("Você possui dependentes?(S/N) ").upper()#Condição para saber se o cliente tem dependente no sistema
        if p_dependente == "S":

            while True:
                cpf_dependente = input("Digite o cpf do dependente: ").strip()#CPF do dependente
                while not cpf_dependente.isdigit() and len(cpf_dependente) == 11:#Verificação para validar o cpf
                    print("Digite apenas números! Deve conter 11 números.")
                    cpf_dependente = input("Digite o cpf do dependente: ").strip()
                limpar_tela()

                nome_dependente = input("Digite o nome do dependente: ").strip()#Nome do dependente
                while not all(parte.isalpha() for parte in nome_dependente.split()):#Verificação para validar o nome
                    print("Digite apenas letras!")
                    nome_dependente = input("Digite o nome do dependente: ").strip()
                limpar_tela()

                idade_dependente = input("Digite a idade do dependente: ").strip()#Idade do dependente
                while not idade_dependente.isdigit():#Verificação para validar a idade
                    print("Digite apenas números!")
                    idade_dependente = input("Digite a idade do dependente: ")
                limpar_tela()
                dependentes.append({"cpf": cpf_dependente, "nome": nome_dependente, "idade": idade_dependente})#Comando para adicionar os dependentes dentro da lista em forma de dicionario

                outro = input("Deseja adicionar outro dependente? (S/N): ").upper()#
                limpar_tela()

                if outro != "S":
                    break
            break
            
        elif p_dependente == "N":
            limpar_tela()
            break
        else:
            print("Opção inválida! Digite S ou N.")

    while True:
        plano = input("Planos:\n""1 - Ouro\n""2 - Diamante\n""3 - Prata\n""4 - Esmeralda\n""Digite o número correspondente ao seu plano:")#Plano do cliiente
        if plano == "1":
            plano = 'Ouro'
            break
        elif plano == "2":
            plano = 'Diamante'
            break
        elif plano == "3":
            plano = 'Prata'
            break
        elif plano == "4":
            plano = 'Esmeralda'
            break
        else:
            print("Opção inválida digite os números de 1-4!")
        limpar_tela()

    valor_plano = calculo(idade, sexo, plano, dependentes)#Função para calcular o valor do plano do cliente de acordo com o tipo
    limpar_tela()
    while True:
        vencimento = input("Digite a data de vencimento do seu plano (dd/mm/aaaa): ").strip()
        try:
            datetime.strptime(vencimento, "%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida")

        limpar_tela()

    dados = {
        "cpf": cpf,
        "nome": nome,
        "sexo": sexo,
        "email": email,
        "idade": idade,
        "titular": titular,
        "telefone": telefone,
        "dependentes": dependentes,
        "plano": plano,
        "valor_plano": valor_plano,
        "vencimento": vencimento
    }#Dicionario para salvar todas as informações 

    salvar_dados(dados)#Função para salvar todos os dados

    return dados

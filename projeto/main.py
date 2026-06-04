from cadastro.cadastro import fazer_cadastro
from others.utilidades import limpar_tela
from cadastro.editor import editar_cliente
from cadastro.listagem_geral import listar_clientes
from cadastro.excluir import excluir_cliente

while True:
  limpar_tela()

  print("====== NÚCLEO SAÚDE ======")
  print("1 - Fazer Cadastro")
  print("2 - Editar Cliente")
  print("3 - Remover Cliente")
  print("4 - Listagem Geral")
  print("0 - Sair")
  print("===========================")
  opcao = input("Escolha uma opção: ")

  #Cadastro

  if opcao == "1":
    dados = fazer_cadastro()

    print("\nCadastro realizado com sucesso!")
    print(f"Cliente: {dados['nome']}")
    print(f"Valor do plano: R$ {dados['valor_plano']:.2f}")
    input("\nPressione Enter para continuar...")
    limpar_tela()
  #Editar Clientes

  elif opcao == "2":
    limpar_tela()
  
    editar_cliente()

    input("\nPressione Enter para continuar...")

  #Remover Cliente

  elif opcao == "3":
    cpf = input("Digite o CPF do Cliente: ")

    excluir_cliente()

    input("\nPressione Enter para continuar...")
  
  #Listagem Geral

  elif opcao == "4":
    limpar_tela()

    listar_clientes()

    input("\nPressione Enter para continuar...")


  #Sair

  elif opcao == "0":
    print("Saindo do sistema...")
    break
  else:
    print("Opção inválida!")
    
    input("\nPressione Enter para continuar...")
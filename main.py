# VARIAVEIS
nome = "Evellyne Vitoria"
tipo_conta = "Corrente"
saldo = 2572.99

opcao = 0

# EXIBIR OS DADOS DO CLIENTE
print("*******************************************")
print("Dados do cliente:")
print(f"\nNome do Cliente:   {nome}")
print(f"Tipo da conta:     {tipo_conta}")
print(f"Saldo inicial:     {saldo}")
print("\n*******************************************")

# MENU DE OPÇÕES
menu = """
** Digite sua opção **

1- Consultar Saldos
2- Transferir valor
3- Receber valor
4- Sair
"""

# LOOP DE OPÇÕES
while opcao != 4:
    print(menu)
    opcao = int(input())  

    if opcao == 1:
        print(f"Seu saldo é {saldo}")

    elif opcao == 2:
        valor = float(input("Qual o valor que deseja Transferir? "))

        if valor > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= valor
            print(f"Novo saldo: {saldo}")

    elif opcao == 3:
        recebido = float(input("Valor recebido: "))
        saldo += recebido
        print(f"Novo saldo: {saldo}")

    elif opcao != 4:
        print("Opção inválida!")

print("Programa encerrado.")

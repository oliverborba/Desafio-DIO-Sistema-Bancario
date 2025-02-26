menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido. Depósitos não podem ser negativos.")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))
        if (
            valor > 0
            and valor <= saldo
            and valor <= limite
            and numero_saques < LIMITE_SAQUES
        ):
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        elif valor > saldo:
            print("Saldo insuficiente.")
        elif valor > limite:
            print("Limite de saque excedido. O limite é de R$ 500 por saque.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques diários atingido.")
        else:
            print("Valor inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")

# Operações Simples
 
menu = """
    Digite [d] para Depositar
    Digite [s] para Sacar
    Digite [e] para Extrato
    Digite [q] para Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao  = input(menu).strip().lower()# Caso o usúario coloque em maiúsculo ou com espaço
    
    if opcao == "d":
        valor = float(input("digite o valor de depósito: "))

        if valor >= 0: 
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
            print('>>>>> Depósito realizado! <<<<<')
        else:
            print("Impossivel Depositar valores negativos")
        # print("Depósito feito!")


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite 
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(">>>>> Saldo insuficiente!")
        elif excedeu_limite:
            print(">>>>> Valor de Saque excedeu seu limite por Saque!")
        elif excedeu_saques:
            print(">>>>> Excedeu o Limíte de saques diário.")
        elif valor > 0   : 
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque:    R$ -{valor:.2f}\n"
            print('>>>>> Saque realizado! <<<<<')
        else:
            print("O valor não pode ser negativo!")


    elif opcao == "e":
        print("\n=========== EXTRATO ============")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================")


    elif opcao == "q" :
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

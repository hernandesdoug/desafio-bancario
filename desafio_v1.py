menu = '''        
[1] - DEPOSITO
[2] - SAQUE
[3] - EXTRATO
[0] - SAIR
'''
oper_mov = 0
saldo = 0 
limite = 500
numero_saques = 0 
LIMITE_SAQUES = 3
extrato = ""

while True:
    opcao = input(menu)

    if opcao == '1':
        valor = float(input("Digite o valor a depositar: "))
        if valor > 0:
            saldo += valor
            oper_mov +=1
            extrato += f'Deposito: R${valor:.2f}\n'
        else:
            print("Digite um valor válido!!")
    elif opcao == '2':
        valor_saque = float(input("Digite o valor a sacar: "))
        if LIMITE_SAQUES == numero_saques:
            print("Você atingiu o limite de saques permitidos por dia!")
        elif valor_saque > limite:
            print("O valor máximo para saque é de R$500,00")
            valor_saque = float(input("Digite o valor a sacar: "))
        elif valor_saque > saldo:
            print("Você não possui saldo suficiente para saque!")
        else:
            saldo -= valor_saque
            numero_saques += 1
            oper_mov +=1 
            extrato += f'Saque: R${valor:.2f}\n'
    elif opcao == '3':
        if oper_mov > 0: 
            print("----------EXTRATO----------------")
            print(extrato)
            print(f'Saldo disponível: R${saldo:.2f}')
        else:
            print('Não foram realizadas movimentações na conta.')
    elif opcao == '0':
        print('Operação encerrada')
        break 
    else:
        print('Opção Inválida, digite a operaçao novamente!')

    
from banco import *
from operacoes.transferencia import transferir
from operacoes.saque import sacar
from operacoes.consulta import consultarSaldo
from operacoes.deposito import depositar

def menu():
    while True:
        print("-----BEM VINDO AO INFINITY BANK-----")
        print("1 - Adicionar conta")
        print("2 - Alterar nome")
        print("3 - Consultar conta")
        print("4 - Remover conta")
        print("5 - Listar contas")
        print("6 - Realizar Saque")
        print("7 - Realizar depósito")
        print("8 - Consultar saldo")
        print("9 - Realizar transferência")
        print("10 - Sair")
        opcao = int(input ("Selecione uma opção: "))

        if opcao == 1:
            nome = input('Digite o nome do cliente: ')
            saldo = float(input('Digite o nome do cliente: '))
        elif opcao == 2:
            conta = int(input('Digite o número da conta: '))
            nome = input('Digite o novo nome: ')
        elif opcao == 3:
            conta = int(input('Digite o núemro da conta: '))
            print(obterConta(conta))
        elif opcao == 4:
            conta = int(input('Digite o núemro da conta: '))
            deletarConta(conta)
        elif opcao == 5:
            listarContas()
        elif opcao == 6:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor que deseja sacar: '))
            sacar(conta, valor)
        elif opcao == 7:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor que deseja sacar: '))
            depositar(conta, valor)
        elif opcao == 8:
            conta = int(input('Digite o número da conta: '))
            consultarSaldo(conta)
        elif opcao == 9:
            contaOrigem = int(input('Informe a conta de origem: '))
            contaDestino = int(input('Informe a conta de origem: '))
            valor = float(input('Digite o valor que deseja trasnferir: '))
            transferir(contaOrigem, contaDestino, valor)
        elif opcao == 10:
            print('Você saiu do sistema!')
            break
        else:
            print('Opção inválida!')

menu()



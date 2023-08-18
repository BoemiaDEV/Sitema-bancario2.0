import textwrap


def menu():
    menu = """\n
    ========== MENU ============\n
    [1]\tDepositar   
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo Usuario
    [6]\tnova conta
    [7]\tSair

=> """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
        if valor > 0:
                saldo += valor
                extrato += f"Depòsito: R$ {valor:.2f}\n"
        else:
                print("valor informado é invalido.")

        return saldo,extrato

def sacar(*,valor, saldo, limite, extrato, numero_saque, LIMITE_SAQUE ):
    
            execedeu_saldo = valor > saldo

            execedeu_limite = valor > limite

            execedeu_saque = valor >= LIMITE_SAQUE

            if execedeu_saldo:
                print("Saldo insuficiente")
            elif execedeu_limite:
                print("o valo desejado execede o limite de saque")

            elif valor > 0:
                saldo -= valor
                extrato += f"saque: R$ {valor:.2f}\n"
                numero_saque += 1

            else:
                print("operação falhou! o valor informado é invalido")

            return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):

    print("\n ############ EXTRATO ############")
    print("\n Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\n saldo: R$ {saldo:.2f}")
    print("####################################")

    return extrato


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def lista_de_contas(usuarios):
    


    return(usuarios)

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    usuarios = []
    conta = []
    LIMITE_SAQUE = 3

    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor que deseja depositar: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor que deseja sacar: "))

            saldo, extrato = sacar(
                valor=valor,
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                LIMITE_SAQUE=LIMITE_SAQUE,
                numero_saque=numero_saque,

            )


        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)
            
        elif opcao == "5":
            lista_de_contas(usuarios)
        elif opcao == "7":
            break

        else:
            print("Opção não reconhecida pelo sistema, por favor selecione novamente a operação desejada")
    
main()

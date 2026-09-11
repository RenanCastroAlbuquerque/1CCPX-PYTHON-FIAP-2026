from model import model_lead
import control

def add_lead():
    name = input('Nome: ')
    email = input('Email: ')
    status = input('Status do fluxo de vendas: ')

    # Validar os dados
    # agora, preciso modelar os dados
    # para isso, vamos usar model.py
    # preciso modelar os dados como m dict

    print(model_lead(name, email, status))

    # com os dadso modelados... preciso enviar para o .json
    # vou usar o control para eniar o dicionaio do lead
    control.create_lead(model_lead(name, email, status))


    print("Lead adicionado (func)")


def list_leads():
    leads = control.read_leads()
    print(leads)
    # Fazer um tabela similida como uma do excel!

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar Leads")
        print("[2] Listar Leads")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            add_lead()
        elif opt == '2':
            list_leads()
        elif opt == '0':
            print("Saindo do programa")
            break
        else:
            print('Opção invalida!')



if __name__ == '__main__':
    main()

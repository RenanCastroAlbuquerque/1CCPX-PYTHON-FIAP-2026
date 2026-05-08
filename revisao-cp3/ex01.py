mensagem = input("Digite uma mensagem: ")

print(mensagem)

for i in mensagem:
    i += mensagem
    print(mensagem)
    mensagem_cancelar = input("Deseja cancelar? ")
    if(mensagem_cancelar == "sim"):
        break;
    elif (mensagem == "não"):
        print(mensagem)
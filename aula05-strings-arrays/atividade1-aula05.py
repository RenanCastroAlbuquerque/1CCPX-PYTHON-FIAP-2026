lista_pessoas = ['Ana', 'Maria', 'Vini', 'Mat']

for i in range(len(lista_pessoas)):
    for j in range(len(lista_pessoas)):
        if (i < j):
            print(lista_pessoas[i], lista_pessoas[j])


print()

# Outra possibilidade:
for a in range(len(lista_pessoas)):
    for b in range(a+1, len(lista_pessoas)):
        print(lista_pessoas[a], lista_pessoas[b])
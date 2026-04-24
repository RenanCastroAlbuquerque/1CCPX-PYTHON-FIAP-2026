for cont_music in range(3):
    print(f'Música {cont_music}')

# Exibir de 1 até 11, pulando de 2 em 2

for i in range(1, 12, 2):
    print(i)

# Atividade 3:

qtd_music = int(input('Digite quantas músicas contem em sua playlist (DB): '))

for i in range(qtd_music):
    print(f'Música {i}')


# Laços Aninhados
# Rep. Encadeadas

for i in range(0, 4):
    for j in range (0, 3, 2):
        print(f'i:{i}, j:{j}')
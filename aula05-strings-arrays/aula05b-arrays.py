lista_frutas = ['Morango', 'Maçã', 'Uva']

print(lista_frutas[1])

lista_frutas.append('Melancia')
print(lista_frutas[3])
print()

for i in range(len(lista_frutas)):
    print(lista_frutas[i])

print()

# For each:
for frutas in lista_frutas:
    print(frutas)
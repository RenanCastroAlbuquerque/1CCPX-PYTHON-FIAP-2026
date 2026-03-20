# Aula02a-variaveis
from numba.core.cgutils import printf

print("Olá Mundo!")

print(7 + 4)
print("7 + 4")
print("7" + "4") #CONCATENAÇÃO DE STRINGS

#Comentarios de 1 linha
'''
    Comentários de 
    multiplas linhas
'''

# VARIÁVEIS
name = "Renan"
idade = 16
peso = 72.4

print( name,"\n", idade,"\n" , peso)
print(f'Oi, {name}')

#INPUT - SIMULAÇÃO DE FORMS NO CMD
name = input("Qual seu nome? ")
idade = int(input("Quantos anos você tem? "))
peso = float(input("Qual seu peso? "))

print(f'Nome: {name} \t idade: {idade} \t peso: {peso}')
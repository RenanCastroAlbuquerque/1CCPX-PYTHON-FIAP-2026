# Escreva um programa que dadas duas ntas de 0 a 10
# Calcula a média aritimética entre elas

def validar_nota (nota):
    while nota < 0 or nota > 10:
        print("A nota deve ser entre 0 a 10!")
        nota = float(input('Digite a nota de maneira correta: '))
    return nota

notaA = float(input('Digite a 1° nota: '))
notaA = validar_nota(notaA)

notaB = float(input('Digite a 2° nota: '))
notaB = validar_nota(notaB)

media = (notaA + notaB) / 2

if media >= 6:
    print(f'Media: {media:.1f}\n Parabéns você foi aprovado!')
elif media >= 5:
    print(f'Media: {media:.1f}\nVocê ficou de recuperação!')
elif media < 3:
    print(f'Media: {media:.1f}\nVocê foi reprovado!')
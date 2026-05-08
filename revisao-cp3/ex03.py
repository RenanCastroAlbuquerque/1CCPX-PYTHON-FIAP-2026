num = int(input("Digite um numero que deseja ver até a tabuada de 25: "))

for i in range (1, 26):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')

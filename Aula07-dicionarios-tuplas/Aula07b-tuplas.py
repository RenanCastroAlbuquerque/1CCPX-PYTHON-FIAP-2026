t = ('a', 'b', 'c')
print(t)
print(t[0])

# GAMBIARRA PARA TROCAR
t1 = 'A',
print(type(t1))

t2 = t1 + t[1:]
print(t2)

# ATRIBUIÇÃO DE TUPLAS
a = 5
b = 10

a, b = b, a
print(a, b)

email = "fulano@gmail.com"
username, dominio = email.split("@")
print(username)
print(dominio)
email = input('Digite uma lista de emails, mas cada email deve estar separada pór virgula: ')
contagem = {}
lista_usuarios = []

for itens in email.split(","):
    emails = itens.strip()

    if "@" in emails:
        username, dominio = emails.split("@", 1)
        contagem[dominio] = contagem.get(dominio, 0) + 1

    print(f"E-mail: {emails} -> Usuário: {username} | Domínio: {dominio} \n Contagem dominio: {contagem}")
    lista_usuarios.append(username)

print("="*30)

t = tuple(contagem.items())

if lista_usuarios:
    primeiro_usuario = lista_usuarios[1]
    ultimo_usuario = lista_usuarios[-1]

    print(f'Primeiro usuario: {primeiro_usuario} | Ultimo usuario: {ultimo_usuario}')


print("="*30)
print(f'Tupla invertida {t[::1]}')

print("="*30)
tupla_usuarios_invertida = tuple(lista_usuarios)[::-1]

print(f'RELATORIO\nQuantidade de e-mails por dominio = {t[::1]}\nLista de usuarios: {username}\nApós troca de posições: {tupla_usuarios_invertida}')
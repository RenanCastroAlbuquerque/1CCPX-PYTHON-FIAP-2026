endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]

# Função que irá verificar se um código http é sucesso ou não
# 200 -> True
# 401 -> False

def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# FUNÇÃO que verifica se tem dois erros seguidos
# nas requisições e UM endpoint

def erros_seguidos(requisicoes):
    for i in range(len(requisicoes) -1):
        codigo_atual = requisicoes[i]
        prox_codigo = requisicoes[i+1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False

# FUNÇÃO para analisar o endpoint
def analisar_endpoint(requisicoes):
    qtd_sucessos = 0 #Inicia como zero

    for codigo in requisicoes:
        if eh_sucesso(codigo):
            qtd_sucessos += 1

    qtd_total_req = len(requisicoes)
    qtd_erros = qtd_total_req - qtd_sucessos
    percentual_sucessos = (qtd_sucessos / qtd_total_req) * 100

    tem_erros_seguidos = erros_seguidos(requisicoes)

    if tem_erros_seguidos:
        classificacao = "CRÍTICO"
    elif percentual_sucessos >= 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"

    return (qtd_sucessos, qtd_erros, percentual_sucessos, classificacao)

# PERCORRENTO A MATRIZ DE STATUS

maior_qtd_erros = -1
endpoint_maior_erro = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    reqs_endpoint = status[i]

    sucessos, erros, percentual, classifacao = analisar_endpoint(reqs_endpoint)

    print(f'Endpoint: {nome_endpoint}')
    print(f'Requisições: {reqs_endpoint}')
    print(f'Sucessos: {sucessos}')
    print(f'Erros: {erros}')
    print(f'% de erros: {percentual}')
    print(f'Classifação: {classifacao}')
    print("-" * 30)
    print()

    if erros > maior_qtd_erros:
        maior_qtd_erros = erros
        endpoint_maior_erro = nome_endpoint

print(f'Endpoint + erros: {endpoint_maior_erro} ({maior_qtd_erros})')
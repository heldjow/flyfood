def calcular_percurso(pontos):
    return sum(abs(pontos[i+1][0] - pontos[i][0]) + abs(pontos[i+1][1] - pontos[i][1])
               for i in range(len(pontos) - 1))

def vizinho_mais_proximo(pontos):
    rota = [pontos[0]]
    nao_visitados = set(pontos[1:])

    while nao_visitados:
        ponto_atual = rota[-1]
        menor_distancia = float('inf')  
        vizinho_proximo = None

        for elemento in nao_visitados:
            distancia = calcular_percurso([ponto_atual, elemento])
            if distancia < menor_distancia:
                menor_distancia = distancia
                vizinho_proximo = elemento

        rota.append(vizinho_proximo)
        nao_visitados.remove(vizinho_proximo)

    rota.append(pontos[0])

    return rota

with open("/home/heldjow/Downloads/flyfood/pontos_de_entrega.txt") as arquivo:
    linhas_lista = arquivo.readlines()

casinhas = {}
chaves_percurso = []
inicio_fim = []

for indice_linha, conteudo_linha in enumerate(linhas_lista):
    conteudo_linha = conteudo_linha.strip()
    for indice_coluna, elemento in enumerate(conteudo_linha.split(sep='|')):
        posicao = (indice_linha, indice_coluna)
        casinhas[posicao] = elemento
        if elemento != '_' and elemento != 'R':
            chaves_percurso.append(posicao)
        if elemento == 'R':
            inicio_fim.append(posicao)

todos_pontos = inicio_fim + chaves_percurso
rota_otima = vizinho_mais_proximo(todos_pontos)
custo_rota = calcular_percurso(rota_otima)

valores_rota_otima = [casinhas[chave] for chave in rota_otima]
string_rota_otima = ",".join(valores_rota_otima)
print(f'\nO menor percurso é: {string_rota_otima} com distância total de {custo_rota} dronômetros')
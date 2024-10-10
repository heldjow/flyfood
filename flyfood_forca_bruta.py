from itertools import permutations

def converter_valores_para_posicoes(dicionario, lista_valores):
    posicoes = []

    for valor in lista_valores:
        for chave, elemento in dicionario.items():
            if elemento == valor:
                posicoes.append(chave)
                break

    return posicoes

def calcular_percurso(pontos):
    percurso_total = 0
    for i in range(len(pontos) - 1):

        ponto_atual = pontos[i]
        ponto_proximo = pontos[i + 1]
        linha_atual, coluna_atual = ponto_atual
        linha_proximo, coluna_proximo = ponto_proximo
        distancia = abs(linha_proximo - linha_atual) + abs(coluna_proximo - coluna_atual)
        percurso_total += distancia

    return percurso_total

arquivo = open("/home/heldjow/Downloads/flyfood/pontos_de_entrega.txt")
linhas_lista = arquivo.readlines()
arquivo.close()

casinhas = {}

for indice_linha, conteudo_linha in enumerate(linhas_lista):
    conteudo_linha = conteudo_linha.strip()
    for indice_coluna, elemento in enumerate(conteudo_linha.split(sep='|')):
        casinhas[(indice_linha, indice_coluna)] = elemento

valores_percurso = []

for elemento in casinhas.values():
    if elemento not in ('_', 'R'):
        valores_percurso.append(elemento)

permutacoes_percurso = permutations(valores_percurso)
menor_percurso = 10000

for permutacao_atual in permutacoes_percurso:
    valores_permutados = ['R'] + list(permutacao_atual) + ['R']
    posicoes_permutadas = converter_valores_para_posicoes(casinhas, valores_permutados)
    percurso_atual = calcular_percurso(posicoes_permutadas)

    if percurso_atual < menor_percurso:
        menor_percurso = percurso_atual
        menor_permutacao = valores_permutados

formatacao_correta = ','.join(menor_permutacao)
print(f'\nO menor percurso é: {formatacao_correta} com distância total de {menor_percurso} dronômetros')
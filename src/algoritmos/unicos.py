"""Maior número que aparece uma única vez (Exercício 5)."""
from algoritmos.metricas import Metricas


def maior_unico_quadratico(arr, metricas=None):
    """Lógica do código fornecido no enunciado, contando as voltas do laço interno. O(N²)."""
    metricas = metricas or Metricas()
    maior = None
    for i in range(len(arr)):
        atual = arr[i]
        contador = 0
        for j in range(len(arr)):           # gargalo: N voltas para cada um dos N elementos
            metricas.iteracoes += 1
            if arr[j] == atual:
                contador += 1
        if contador == 1:
            if (maior is None) or (atual > maior):
                maior = atual
    return maior


def maior_unico(arr, metricas=None):
    """Mesmo resultado em O(N): conta as ocorrências num dicionário e depois escolhe o maior único."""
    metricas = metricas or Metricas()
    ocorrencias = {}
    for valor in arr:
        metricas.iteracoes += 1
        ocorrencias[valor] = ocorrencias.get(valor, 0) + 1

    maior = None
    for valor, quantidade in ocorrencias.items():
        metricas.iteracoes += 1
        if quantidade == 1 and (maior is None or valor > maior):
            maior = valor
    return maior

"""Busca linear e busca binária (Aula 2)."""
from algoritmos.metricas import Metricas

NAO_ENCONTRADO = -1


def busca_linear(seq, alvo, metricas=None, ao_comparar=None):
    """Índice da primeira ocorrência de alvo, ou NAO_ENCONTRADO. Conta cada seq[i] == alvo. O(N)."""
    metricas = metricas or Metricas()
    for indice, valor in enumerate(seq):
        if ao_comparar:
            ao_comparar(indice, valor)
        metricas.comparacoes += 1
        if valor == alvo:
            return indice
    return NAO_ENCONTRADO


def busca_binaria(seq_ordenada, alvo, metricas=None, ao_inspecionar=None):
    """Índice de alvo numa sequência crescente, ou NAO_ENCONTRADO. O(log N).

    Cada volta conta a comparação de igualdade com o meio e, se o alvo não está ali, a de direção.
    """
    metricas = metricas or Metricas()
    inicio, fim = 0, len(seq_ordenada) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        metricas.iteracoes += 1
        if ao_inspecionar:
            ao_inspecionar(inicio, fim, meio)

        metricas.comparacoes += 1
        if seq_ordenada[meio] == alvo:
            return meio

        metricas.comparacoes += 1
        if alvo < seq_ordenada[meio]:
            fim = meio - 1          # o alvo só pode estar à esquerda do meio
        else:
            inicio = meio + 1       # o alvo só pode estar à direita do meio
    return NAO_ENCONTRADO

"""Conferência dos resultados de ordenação, usada nos scripts e nos testes."""
from collections import Counter

from algoritmos.ordenacao import identidade


def esta_ordenada(seq, chave=identidade):
    return all(chave(seq[i]) <= chave(seq[i + 1]) for i in range(len(seq) - 1))


def mesma_colecao(a, b):
    """Mesmos elementos com as mesmas quantidades, em qualquer ordem."""
    return Counter(a) == Counter(b)


def ordenacao_correta(entrada, saida, chave=identidade):
    """A saída está em ordem e é uma permutação da entrada."""
    return esta_ordenada(saida, chave) and mesma_colecao(entrada, saida)

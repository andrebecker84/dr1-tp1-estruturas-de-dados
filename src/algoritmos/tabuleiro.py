"""Tabuleiro de xadrez e grãos de arroz (Exercício 6): o quadrado n tem 2^(n-1) grãos."""
from algoritmos.metricas import Metricas

QUADRADOS = 64
MAX_POR_QUADRADO = 2 ** (QUADRADOS - 1)     # grãos no quadrado 64
TOTAL_DO_TABULEIRO = 2 ** QUADRADOS - 1     # soma dos 64 quadrados
MENSAGEM_LIMITE = "valor excede o limite do tabuleiro"


def menor_quadrado(qtd_graos, metricas=None):
    """Menor quadrado com pelo menos qtd_graos grãos, ou MENSAGEM_LIMITE. O(log Q), no máximo 64 voltas."""
    if not isinstance(qtd_graos, int) or qtd_graos <= 0:
        raise ValueError("qtd_graos deve ser um inteiro positivo")
    metricas = metricas or Metricas()

    graos = 1
    for quadrado in range(1, QUADRADOS + 1):
        metricas.iteracoes += 1
        if graos >= qtd_graos:
            return quadrado
        graos *= 2                          # o próximo quadrado tem o dobro
    return MENSAGEM_LIMITE

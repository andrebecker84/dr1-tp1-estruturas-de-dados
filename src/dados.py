"""Entradas dos experimentos. A semente é fixa: toda execução gera os mesmos dados."""
import random
from enum import StrEnum

SEMENTE = 42
ARRAY_DA_AULA_2 = (2, 4, 6, 8, 10, 12, 13)     # quiz da Aula 2, usado nos Exercícios 3 e 4
TAMANHOS_DO_BUBBLE = (10, 100, 1_000)           # os Exercícios 11 e 12 usam os mesmos dados


class Cenario(StrEnum):
    ORDENADA = "ordenada"
    ALEATORIA = "aleatória"
    INVERSA = "inversa"


def inteiros_distintos(n, semente=SEMENTE):
    """n inteiros distintos entre 1 e 10n, fora de ordem."""
    random.seed(semente)
    return random.sample(range(1, 10 * n + 1), n)


def lista_no_cenario(n, cenario, semente=SEMENTE):
    """Os inteiros de 1 a n na ordem do cenário."""
    lista = list(range(1, n + 1))
    if cenario is Cenario.INVERSA:
        lista.reverse()
    elif cenario is Cenario.ALEATORIA:
        random.seed(semente)
        random.shuffle(lista)
    return lista

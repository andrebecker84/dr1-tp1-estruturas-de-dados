"""Bubble Sort (Aula 3), com e sem parada antecipada, e o Cocktail Sort.

Todas as funções ordenam uma cópia e devolvem a lista nova. A função chave define a ordem.
"""
from algoritmos.metricas import Metricas


def identidade(valor):
    return valor


def bubble_sort(seq, chave=identidade, metricas=None, ao_fim_da_passagem=None):
    """Versão clássica: sempre N(N - 1)/2 comparações. O(N²)."""
    return _bubble(seq, chave, metricas, ao_fim_da_passagem, parar_sem_trocas=False)


def bubble_sort_com_parada(seq, chave=identidade, metricas=None, ao_fim_da_passagem=None):
    """Para quando uma passagem não troca nada. Melhor caso O(N), pior caso O(N²)."""
    return _bubble(seq, chave, metricas, ao_fim_da_passagem, parar_sem_trocas=True)


def cocktail_sort(seq, chave=identidade, metricas=None):
    """Bubble Sort nos dois sentidos: a ida leva o maior até 'direito', a volta leva o menor até 'esquerdo'."""
    metricas = metricas or Metricas()
    lista = list(seq)
    esquerdo, direito = 0, len(lista) - 1
    while esquerdo < direito:
        if not _passagem(lista, range(esquerdo, direito), chave, metricas):
            break
        direito -= 1
        if not _passagem(lista, range(direito - 1, esquerdo - 1, -1), chave, metricas):
            break
        esquerdo += 1
    return lista


def _bubble(seq, chave, metricas, ao_fim_da_passagem, parar_sem_trocas):
    metricas = metricas or Metricas()
    lista = list(seq)
    for ultimo in range(len(lista) - 1, 0, -1):     # a cada passagem, o maior restante vai para 'ultimo'
        trocou = _passagem(lista, range(ultimo), chave, metricas)
        if ao_fim_da_passagem:
            ao_fim_da_passagem(lista, metricas)
        if parar_sem_trocas and not trocou:
            break
    return lista


def _passagem(lista, posicoes, chave, metricas):
    """Compara cada par (i, i + 1) e troca os que estão fora de ordem. Devolve se houve troca."""
    metricas.passagens += 1
    trocou = False
    for i in posicoes:
        metricas.comparacoes += 1
        if chave(lista[i]) > chave(lista[i + 1]):
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            metricas.trocas += 1
            trocou = True
    return trocou

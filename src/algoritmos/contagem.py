"""Funções com os nomes e retornos pedidos no Exercício 13: (resultado, comparações).

São adaptadores finos sobre o núcleo (busca.py e ordenacao.py), para o resto do código não
depender do formato do enunciado. O Exercício 14 compara estas funções com o código original.
"""
from algoritmos.busca import busca_binaria, busca_linear
from algoritmos.metricas import medir
from algoritmos.ordenacao import bubble_sort


def linear_search_count(arr, target):
    index, metricas = medir(busca_linear, arr, target)
    return index, metricas.comparacoes


def binary_search_count(sorted_arr, target):
    index, metricas = medir(busca_binaria, sorted_arr, target)
    return index, metricas.comparacoes


def bubble_sort_count(arr):
    sorted_arr, metricas = medir(bubble_sort, arr)
    return sorted_arr, metricas.comparacoes

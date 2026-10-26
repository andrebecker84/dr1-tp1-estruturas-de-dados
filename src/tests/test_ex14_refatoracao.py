"""Teste do Exercício 14: a versão refatorada produz exatamente o mesmo resultado da original.

    cd src && python3 -m unittest -v tests.test_ex14_refatoracao
"""
import random
import unittest

from algoritmos.contagem import binary_search_count, bubble_sort_count


# ---------------------------------------------------- código original, sem alterações
def f(a, t):
    c = 0
    i = 0
    j = len(a) - 1
    r = -1
    while i <= j:
        m = (i + j) // 2
        c = c + 1
        if a[m] == t:
            r = m
            break
        c = c + 1
        if t < a[m]:
            j = m - 1
        else:
            i = m + 1
    return r, c

def h(arr):
    b = arr[:]
    n = len(b)
    k = 0
    for last in range(n - 1, 0, -1):
        for p in range(last):
            k += 1
            if b[p] > b[p + 1]:
                tmp = b[p]
                b[p] = b[p + 1]
                b[p + 1] = tmp
    return b, k


# ------------------------------------------------------------------------ testes
def lista_aleatoria():
    return [random.randint(-20, 20) for _ in range(random.randint(0, 40))]


def listas_de_teste():
    """Casos de borda + 200 listas aleatórias (com repetidos) de tamanho 0 a 40."""
    random.seed(42)
    bordas = [[], [7], [2, 1], [1, 2], [3, 3, 3], list(range(10)), list(range(10, 0, -1))]
    return bordas + [lista_aleatoria() for _ in range(200)]


class TestEx14(unittest.TestCase):

    def test_bubble_igual_ao_original(self):
        for lista in listas_de_teste():
            with self.subTest(lista=lista):
                self.assertEqual(bubble_sort_count(lista), h(lista))

    def test_bubble_nao_altera_entrada(self):
        lista = [5, 2, 9, 1]
        bubble_sort_count(lista)
        self.assertEqual(lista, [5, 2, 9, 1])

    def test_binaria_igual_ao_original(self):
        for lista in listas_de_teste():
            ordenada, _ = h(lista)                 # ordenação sem sorted()/.sort()
            for alvo in set(ordenada) | {-99, 0, 99}:
                with self.subTest(lista=ordenada, alvo=alvo):
                    self.assertEqual(binary_search_count(ordenada, alvo), f(ordenada, alvo))

    def test_exemplos_das_aulas(self):
        self.assertEqual(binary_search_count([2, 4, 6, 8, 10, 12, 13], 8), (3, 1))
        self.assertEqual(bubble_sort_count([4, 2, 7, 1, 3]), ([1, 2, 3, 4, 7], 10))


if __name__ == "__main__":
    unittest.main(verbosity=2)

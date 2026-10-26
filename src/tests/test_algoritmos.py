"""Testes do núcleo (algoritmos/): resultados, contadores e casos de borda.

    cd src && python3 -m unittest discover -s tests -t . -v
"""
import random
import unittest

from algoritmos.busca import NAO_ENCONTRADO, busca_binaria, busca_linear
from algoritmos.metricas import medir
from algoritmos.ordenacao import bubble_sort, bubble_sort_com_parada, cocktail_sort
from algoritmos.tabuleiro import MAX_POR_QUADRADO, MENSAGEM_LIMITE, menor_quadrado
from algoritmos.texto import chave_alfabetica
from algoritmos.unicos import maior_unico, maior_unico_quadratico
from verificacao import ordenacao_correta


def lista_aleatoria(tamanho_maximo=30):
    return [random.randint(-10, 10) for _ in range(random.randint(0, tamanho_maximo))]


def listas_aleatorias(quantidade=100):
    random.seed(7)
    return [lista_aleatoria() for _ in range(quantidade)]


class TestBusca(unittest.TestCase):

    def test_linear_conta_ate_achar(self):
        indice, metricas = medir(busca_linear, [5, 3, 8], 8)
        self.assertEqual((indice, metricas.comparacoes), (2, 3))

    def test_linear_ausente_percorre_tudo(self):
        indice, metricas = medir(busca_linear, [5, 3, 8], 9)
        self.assertEqual((indice, metricas.comparacoes), (NAO_ENCONTRADO, 3))

    def test_binaria_acha_todos_os_presentes(self):
        seq = list(range(0, 40, 2))
        for indice, valor in enumerate(seq):
            self.assertEqual(busca_binaria(seq, valor), indice)

    def test_binaria_ausente_e_lista_vazia(self):
        self.assertEqual(busca_binaria([1, 3, 5], 4), NAO_ENCONTRADO)
        self.assertEqual(busca_binaria([], 4), NAO_ENCONTRADO)

    def test_binaria_respeita_log_n(self):
        seq = list(range(1_000))
        self.assertLessEqual(medir(busca_binaria, seq, -1)[1].iteracoes, 10)


class TestOrdenacao(unittest.TestCase):

    def test_as_tres_versoes_ordenam(self):
        for algoritmo in (bubble_sort, bubble_sort_com_parada, cocktail_sort):
            for lista in listas_aleatorias():
                with self.subTest(algoritmo=algoritmo.__name__, lista=lista):
                    self.assertTrue(ordenacao_correta(lista, algoritmo(lista)))

    def test_nao_alteram_a_entrada(self):
        lista = [3, 1, 2]
        for algoritmo in (bubble_sort, bubble_sort_com_parada, cocktail_sort):
            algoritmo(lista)
            self.assertEqual(lista, [3, 1, 2])

    def test_classico_faz_n_n_menos_1_sobre_2_comparacoes(self):
        for n in (0, 1, 2, 10, 50):
            metricas = medir(bubble_sort, list(range(n)))[1]
            self.assertEqual(metricas.comparacoes, n * (n - 1) // 2)

    def test_parada_antecipada_na_lista_ordenada(self):
        metricas = medir(bubble_sort_com_parada, list(range(100)))[1]
        self.assertEqual((metricas.comparacoes, metricas.passagens), (99, 1))

    def test_trocas_sao_as_inversoes(self):
        metricas = medir(bubble_sort, [3, 2, 1])[1]
        self.assertEqual(metricas.trocas, 3)

    def test_chave_alfabetica(self):
        palavras = ["Zebra", "ábaco", "banana"]
        self.assertEqual(bubble_sort(palavras, chave=chave_alfabetica), ["ábaco", "banana", "Zebra"])
        self.assertEqual(bubble_sort(palavras), ["Zebra", "banana", "ábaco"])


class TestExercicios5e6(unittest.TestCase):

    def test_maior_unico_igual_ao_original(self):
        for lista in listas_aleatorias():
            with self.subTest(lista=lista):
                self.assertEqual(maior_unico(lista), maior_unico_quadratico(lista))

    def test_maior_unico_bordas(self):
        self.assertIsNone(maior_unico([]))
        self.assertIsNone(maior_unico([2, 2]))
        self.assertEqual(maior_unico([10, 10, 9]), 9)

    def test_menor_quadrado(self):
        casos = {1: 1, 2: 2, 4: 3, 8: 4, 1_000: 11, 1_000_000: 21, MAX_POR_QUADRADO: 64}
        for qtd, quadrado in casos.items():
            self.assertEqual(menor_quadrado(qtd), quadrado)
        self.assertEqual(menor_quadrado(MAX_POR_QUADRADO + 1), MENSAGEM_LIMITE)

    def test_menor_quadrado_rejeita_entrada_invalida(self):
        for invalida in (0, -1, 2.5, "10"):
            with self.assertRaises(ValueError):
                menor_quadrado(invalida)


if __name__ == "__main__":
    unittest.main()

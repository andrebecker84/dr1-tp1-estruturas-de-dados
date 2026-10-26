"""Exercício 14: refatoração das funções f (busca binária) e h (Bubble Sort) do enunciado.

O código refatorado ficou no núcleo, onde os outros exercícios também o usam:
  f -> algoritmos.busca.busca_binaria       + algoritmos.contagem.binary_search_count
  h -> algoritmos.ordenacao.bubble_sort     + algoritmos.contagem.bubble_sort_count
As funções de contagem mantêm a assinatura e o retorno do original: (resultado, comparações).
O teste tests/test_ex14_refatoracao.py compara as duas versões.
"""
from algoritmos.contagem import binary_search_count, bubble_sort_count

EXEMPLO_DA_BUSCA = [2, 4, 6, 8, 10, 12, 13]      # array dos Exercícios 3 e 4
EXEMPLO_DA_ORDENACAO = [4, 2, 7, 1, 3]           # exemplo do slide da Aula 3


def main():
    resultados = {
        f"binary_search_count({EXEMPLO_DA_BUSCA}, 8)": binary_search_count(EXEMPLO_DA_BUSCA, 8),
        f"bubble_sort_count({EXEMPLO_DA_ORDENACAO})": bubble_sort_count(EXEMPLO_DA_ORDENACAO),
    }
    largura = max(len(chamada) for chamada in resultados)
    for chamada, resultado in resultados.items():
        print(f"{chamada:<{largura}} = {resultado}")


if __name__ == "__main__":
    main()

"""Exercício 9: Bubble Sort numérico em ordem crescente, com verificação da saída."""
import random

from algoritmos.ordenacao import bubble_sort
from apresentacao.terminal import compacta, ok, titulo
from dados import SEMENTE
from verificacao import ordenacao_correta

LISTAS_ALEATORIAS = 500
TAMANHO_MAXIMO = 60


def casos_de_teste():
    return [
        ("desordenada", [64, 34, 25, 12, 22, 11, 90]),
        ("já ordenada", [1, 2, 3, 4, 5, 6, 7]),
        ("ordem inversa", [9, 8, 7, 6, 5, 4, 3, 2, 1]),
        ("com repetidos", [3, 1, 2, 3, 1, 2]),
        ("negativos", [0, -3, 5, -1, -8, 2]),
        ("float e int", [2.5, -1, 3.14, 0, 2]),
        ("vazia", []),
        ("um elemento", [42]),
        ("aleatória N=12", random.sample(range(100), 12)),
    ]


def mostrar_casos():
    titulo("Exercício 9: Bubble Sort numérico")
    todos_ok = True
    for nome, entrada in casos_de_teste():
        copia = entrada[:]
        saida = bubble_sort(entrada)
        todos_ok = todos_ok and ordenacao_correta(entrada, saida) and entrada == copia
        print(f"{nome:<15} {compacta(entrada):<46} -> {compacta(saida)}")
    print()
    ok(todos_ok, "saídas em ordem crescente, mesmos elementos, entrada original intacta")


def lista_aleatoria():
    return [random.randint(-1000, 1000) for _ in range(random.randint(0, TAMANHO_MAXIMO))]


def conferir_com_sorted():
    lote = [lista_aleatoria() for _ in range(LISTAS_ALEATORIAS)]
    iguais = all(bubble_sort(lista) == sorted(lista) for lista in lote)
    ok(iguais, f"{LISTAS_ALEATORIAS} listas aleatórias (N de 0 a {TAMANHO_MAXIMO}) iguais ao sorted() do Python")


def main():
    random.seed(SEMENTE)
    mostrar_casos()
    conferir_com_sorted()


if __name__ == "__main__":
    main()

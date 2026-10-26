"""Exercício 8: Bubble Sort bidirecional (Cocktail Sort) comparado com o Bubble Sort tradicional."""
import random

from algoritmos.metricas import medir
from algoritmos.ordenacao import bubble_sort_com_parada, cocktail_sort
from apresentacao.terminal import compacta, ok, tabela, titulo
from dados import SEMENTE
from verificacao import ordenacao_correta


def casos_de_teste():
    random.seed(SEMENTE)
    return {
        "aleatória": random.sample(range(1, 100), 12),
        "já ordenada": list(range(1, 13)),
        "ordem inversa": list(range(12, 0, -1)),
        "com repetidos": [5, 1, 4, 1, 5, 9, 2, 6, 5, 3],
        "tartaruga (menor no fim)": [*range(2, 13), 1],
        "coelho (maior no início)": [12, *range(1, 12)],
        "vazia": [],
        "um elemento": [7],
    }


def mostrar_resultados(casos):
    titulo("Exercício 8: Cocktail Sort: resultados")
    todos_ok = True
    for nome, entrada in casos.items():
        saida = cocktail_sort(entrada)
        todos_ok = todos_ok and ordenacao_correta(entrada, saida)
        print(f"{nome:<25} {compacta(entrada):<36} -> {compacta(saida)}")
    ok(todos_ok, "todas as saídas ordenadas e com os mesmos elementos da entrada")


def mostrar_comparacao(casos):
    titulo("Bubble tradicional x bidirecional (ambos com parada antecipada)")
    linhas = []
    for nome, entrada in casos.items():
        bubble = medir(bubble_sort_com_parada, entrada)[1]
        cocktail = medir(cocktail_sort, entrada)[1]
        linhas.append([nome, bubble.passagens, bubble.comparacoes, cocktail.passagens, cocktail.comparacoes])
    cabecalho = ["entrada", "passagens bubble", "comparações bubble", "passagens cocktail", "comparações cocktail"]
    tabela(cabecalho, linhas)


def main():
    casos = casos_de_teste()
    mostrar_resultados(casos)
    print()
    mostrar_comparacao(casos)


if __name__ == "__main__":
    main()

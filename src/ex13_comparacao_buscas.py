"""Exercício 13: busca linear x busca binária, com Bubble Sort quando a lista não está ordenada.

As funções da Parte A (linear_search_count, binary_search_count e bubble_sort_count) estão em
algoritmos/contagem.py. Na binária, cada volta conta a comparação de igualdade com o meio e, se o
alvo não está ali, a de direção: a mesma contagem do código do Exercício 14.
"""
import math

from algoritmos.busca import NAO_ENCONTRADO
from algoritmos.contagem import binary_search_count, bubble_sort_count, linear_search_count
from apresentacao.terminal import compacta, ok, tabela, titulo
from dados import Cenario, lista_no_cenario
from verificacao import esta_ordenada

N = 31
TARGET_ABSENT = -1
CUSTO_DO_BUBBLE = N * (N - 1) // 2
EXEMPLOS_DE_K = (1, 10, 100)


def criar_listas():
    return {"arr_sorted": lista_no_cenario(N, Cenario.ORDENADA),
            "arr_reverse": lista_no_cenario(N, Cenario.INVERSA),
            "arr_random": lista_no_cenario(N, Cenario.ALEATORIA)}


def comparar_buscas(nome, arr):
    """Linhas da tabela para os três alvos de uma lista. Fora de ordem, ordena antes da binária."""
    ordenada, custo_ordenacao = (arr, 0) if esta_ordenada(arr) else bubble_sort_count(arr)
    alvos = {"first": arr[0], "middle": arr[N // 2], "absent": TARGET_ABSENT}
    linhas = []
    for rotulo, target in alvos.items():
        linear = linear_search_count(arr, target)[1]
        binaria = binary_search_count(ordenada, target)[1]
        bubble, total = (custo_ordenacao, custo_ordenacao + binaria) if custo_ordenacao else ("-", "-")
        linhas.append([nome, rotulo, target, linear, binaria, bubble, total])
    return linhas


def mostrar_verificacoes(linhas, arr_random):
    titulo("Verificações")
    pior_binaria = 2 * (math.floor(math.log2(N)) + 1)
    binaria_ok = max(linha[4] for linha in linhas) <= pior_binaria
    linear_ok = all(linha[3] == N for linha in linhas if linha[1] == "absent")
    bubble_ok = all(linha[5] in ("-", CUSTO_DO_BUBBLE) for linha in linhas)
    nao_achado = next(v for v in arr_random if binary_search_count(arr_random, v)[0] == NAO_ENCONTRADO)

    ok(binaria_ok, f"binária <= 2·(int(log2 N) + 1) = {pior_binaria} comparações em todos os casos")
    ok(linear_ok, f"linear com alvo ausente = N = {N}")
    ok(bubble_ok, f"bubble sort = N(N-1)/2 = {CUSTO_DO_BUBBLE} comparações")
    aviso = f"binária direto em arr_random NÃO acha o {nao_achado}, que está na lista (pré-requisito violado)"
    ok(nao_achado in arr_random, aviso)


def mostrar_ponto_de_equilibrio(arr_sorted):
    titulo("Ponto de equilíbrio: k buscas no pior caso (alvo ausente)")
    binaria = binary_search_count(arr_sorted, TARGET_ABSENT)[1]
    equilibrio = CUSTO_DO_BUBBLE // (N - binaria) + 1
    linhas = []
    for k in sorted({*EXEMPLOS_DE_K, equilibrio - 1, equilibrio}):
        so_linear, ordenando = k * N, CUSTO_DO_BUBBLE + k * binaria
        linhas.append([k, so_linear, ordenando, "binária" if ordenando < so_linear else "linear"])
    tabela(["k buscas", "linear (k·N)", "bubble + k·binária", "mais barata"], linhas)
    print(f"ordenar com Bubble Sort compensa a partir de k = {equilibrio} buscas na mesma lista")


def main():
    listas = criar_listas()
    titulo(f"Exercício 13: listas com N = {N}")
    for nome, arr in listas.items():
        print(f"{nome:<12} {compacta(arr)}")

    print()
    titulo("Comparações por lista e alvo")
    linhas = [linha for nome, arr in listas.items() for linha in comparar_buscas(nome, arr)]
    tabela(["lista", "alvo", "valor", "linear", "binária", "bubble", "bubble+binária"], linhas, "<<>>>>>")
    print()
    mostrar_verificacoes(linhas, listas["arr_random"])
    print()
    mostrar_ponto_de_equilibrio(listas["arr_sorted"])


if __name__ == "__main__":
    main()

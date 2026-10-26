"""Exercício 11: Bubble Sort clássico com contagem de comparações e trocas."""
from algoritmos.metricas import medir
from algoritmos.ordenacao import bubble_sort
from apresentacao.terminal import milhar, ok, tabela, titulo
from dados import TAMANHOS_DO_BUBBLE, Cenario, lista_no_cenario


def comparacoes_teoricas(n):
    return n * (n - 1) // 2


def mostrar_contagens():
    titulo("Exercício 11: Bubble Sort clássico: comparações e trocas")
    linhas, todos_ok = [], True
    for n in TAMANHOS_DO_BUBBLE:
        for cenario in Cenario:
            saida, metricas = medir(bubble_sort, lista_no_cenario(n, cenario))
            esperado = comparacoes_teoricas(n)
            todos_ok = todos_ok and saida == list(range(1, n + 1)) and metricas.comparacoes == esperado
            contagens = [metricas.comparacoes, metricas.trocas, esperado]
            linhas.append([milhar(n), cenario, *map(milhar, contagens)])
    tabela(["N", "cenário", "comparações", "trocas", "N(N-1)/2"], linhas)
    ok(todos_ok, "saídas ordenadas; comparações = N(N-1)/2 em todos os cenários")


def mostrar_crescimento():
    titulo("Crescimento: N multiplicado por 10")
    linhas, anterior = [], None
    for n in TAMANHOS_DO_BUBBLE:
        metricas = medir(bubble_sort, lista_no_cenario(n, Cenario.INVERSA))[1]
        fator = f"x{metricas.comparacoes / anterior:.0f}" if anterior else "-"
        linhas.append([milhar(n), milhar(metricas.comparacoes + metricas.trocas), fator])
        anterior = metricas.comparacoes
    tabela(["N", "passos no pior caso (comp. + trocas)", "comparações vs. N anterior"], linhas)
    print("N x10  ->  passos x~100: crescimento quadrático, O(N²)")


def main():
    mostrar_contagens()
    print()
    mostrar_crescimento()


if __name__ == "__main__":
    main()

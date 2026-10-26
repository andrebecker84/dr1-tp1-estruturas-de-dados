"""Exercício 1: busca linear instrumentada em 10.000 inteiros distintos e fora de ordem."""
from algoritmos.busca import busca_linear
from algoritmos.metricas import medir
from apresentacao.terminal import milhar, ok, tabela, titulo
from dados import inteiros_distintos
from verificacao import esta_ordenada

TAMANHO = 10_000
TAMANHOS_DO_PIOR_CASO = (1_000, 10_000, 100_000)
AUSENTE = -1                                    # os valores gerados vão de 1 a 10N


def buscar(seq, alvo):
    """Devolve (índice, comparações) da busca linear."""
    indice, metricas = medir(busca_linear, seq, alvo)
    return indice, metricas.comparacoes


def mostrar_busca_pedida(arr):
    titulo(f"Exercício 1: busca linear em {milhar(TAMANHO)} inteiros distintos (não ordenados)")
    print(f"primeiros elementos: {arr[:8]} ...")
    ok(len(set(arr)) == TAMANHO, f"{milhar(TAMANHO)} valores distintos")
    ok(not esta_ordenada(arr), "array não ordenado")

    alvo = arr[0]
    indice, comparacoes = buscar(arr, alvo)
    print(f"\nalvo = arr[0] = {alvo}  ->  índice {indice}, comparações: {comparacoes}")
    ok(indice == 0 and comparacoes == 1, "elemento na 1ª posição: 1 comparação (melhor caso)")


def mostrar_outras_posicoes(arr):
    titulo("Mesma busca para outras posições do alvo")
    meio = arr[TAMANHO // 2]
    casos = {"primeira posição": arr[0], "meio (N//2)": meio, "última posição": arr[-1], "ausente": AUSENTE}
    linhas = []
    for nome, alvo in casos.items():
        indice, comparacoes = buscar(arr, alvo)
        linhas.append([nome, indice, milhar(comparacoes)])
    tabela(["caso", "índice", "comparações"], linhas)


def mostrar_pior_caso_por_tamanho():
    titulo("Pior caso (alvo ausente) com N crescente")
    linhas = []
    for n in TAMANHOS_DO_PIOR_CASO:
        _, comparacoes = buscar(inteiros_distintos(n), AUSENTE)
        linhas.append([milhar(n), milhar(comparacoes), f"{comparacoes / n:.0f}·N"])
    tabela(["N", "comparações", "razão"], linhas)


def main():
    arr = inteiros_distintos(TAMANHO)
    mostrar_busca_pedida(arr)
    print()
    mostrar_outras_posicoes(arr)
    print()
    mostrar_pior_caso_por_tamanho()


if __name__ == "__main__":
    main()

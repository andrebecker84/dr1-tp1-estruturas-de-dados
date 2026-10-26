"""Exercício 5: maior número único, da versão fornecida O(N²) para uma versão O(N)."""
import random

from algoritmos.metricas import medir
from algoritmos.unicos import maior_unico, maior_unico_quadratico
from apresentacao.terminal import milhar, ok, tabela, titulo
from dados import SEMENTE

CASOS_DE_BORDA = (
    [5, 7, 3, 9, 4, 9, 8, 3, 1],        # 9 e 3 repetem: o maior único é 8
    [2, 2, 3, 3],                       # nenhum único: None
    [],                                 # vazia: None
    [42],                               # um elemento
    [-5, -1, -1, -7],                   # negativos: o maior único é -5
    [10, 10, 9],                        # o maior valor repete: a resposta é 9
)
LISTAS_ALEATORIAS = 50
TAMANHO_ALEATORIO = 200
TAMANHOS = (10, 100, 1_000, 5_000)


def mostrar_equivalencia():
    titulo("Exercício 5: maior número único: original O(N²) x otimizada O(N)")
    linhas = [[str(caso), maior_unico_quadratico(caso), maior_unico(caso)] for caso in CASOS_DE_BORDA]
    tabela(["entrada", "original", "otimizada"], linhas, "<>>")

    aleatorias = [[random.randint(0, 50) for _ in range(TAMANHO_ALEATORIO)] for _ in range(LISTAS_ALEATORIAS)]
    casos = [*CASOS_DE_BORDA, *aleatorias]
    iguais = all(maior_unico_quadratico(caso) == maior_unico(caso) for caso in casos)
    ok(iguais, f"mesmo resultado nos {len(casos)} casos (6 acima + 50 aleatórios com N = {TAMANHO_ALEATORIO})")


def mostrar_passos_por_tamanho():
    titulo("Passos executados em função de N")
    linhas = []
    for n in TAMANHOS:
        arr = [random.randint(0, n) for _ in range(n)]
        original = medir(maior_unico_quadratico, arr)[1].iteracoes
        otimizada = medir(maior_unico, arr)[1].iteracoes
        linhas.append([milhar(n), milhar(original), milhar(otimizada), f"{original / otimizada:.0f}x"])
    tabela(["N", "original (N²)", "otimizada (≤ 2N)", "redução"], linhas)


def main():
    random.seed(SEMENTE)
    mostrar_equivalencia()
    print()
    mostrar_passos_por_tamanho()


if __name__ == "__main__":
    main()

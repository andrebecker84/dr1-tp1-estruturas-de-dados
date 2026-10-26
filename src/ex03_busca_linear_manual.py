"""Exercício 3: busca linear passo a passo por 8 em [2, 4, 6, 8, 10, 12, 13]."""
from algoritmos.busca import busca_linear
from algoritmos.metricas import medir
from apresentacao.terminal import ok, tabela, titulo
from dados import ARRAY_DA_AULA_2

ALVO = 8
AUSENTE = 7


def rastrear(seq, alvo):
    """Busca linear guardando cada (índice, valor) comparado. Devolve (índice, comparações, rastro)."""
    rastro = []
    indice, metricas = medir(busca_linear, seq, alvo, ao_comparar=lambda *par: rastro.append(par))
    return indice, metricas.comparacoes, rastro


def mostrar_rastro():
    titulo(f"Exercício 3: busca linear por {ALVO} em {list(ARRAY_DA_AULA_2)}  (N = {len(ARRAY_DA_AULA_2)})")
    indice, comparacoes, rastro = rastrear(ARRAY_DA_AULA_2, ALVO)
    linhas = [[passo, i, valor, f"{valor} == {ALVO}?", "sim" if valor == ALVO else "não"]
              for passo, (i, valor) in enumerate(rastro, 1)]
    tabela(["passo", "índice", "valor", "comparação", "igual?"], linhas, ">>>^^")
    print(f"\nencontrado no índice {indice} após {comparacoes} comparações")
    ok(comparacoes == indice + 1 == 4, "comparações = posição do alvo + 1 = 4")


def mostrar_todos_os_alvos():
    titulo("Passos da busca linear para cada alvo possível")
    linhas = [[alvo, *rastrear(ARRAY_DA_AULA_2, alvo)[:2]] for alvo in (*ARRAY_DA_AULA_2, AUSENTE)]
    tabela(["alvo", "índice", "comparações"], linhas)
    print(f"pior caso (último ou ausente): N = {len(ARRAY_DA_AULA_2)} comparações  ->  O(N)")


def main():
    mostrar_rastro()
    print()
    mostrar_todos_os_alvos()


if __name__ == "__main__":
    main()

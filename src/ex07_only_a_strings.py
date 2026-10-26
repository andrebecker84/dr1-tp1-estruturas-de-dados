"""Exercício 7: análise Big O de only_a_strings.

A função fornecida fica intacta. only_a_strings_medida tem a mesma estrutura e conta as voltas do
laço e as operações O(1) do modelo de custo do enunciado, para conferir a análise na prática.
"""
import random

from apresentacao.terminal import milhar, ok, tabela, titulo
from dados import SEMENTE

PALAVRAS = ("abacate", "banana", "amora", "uva", "acerola", "kiwi", "")
TAMANHOS = (10, 100, 1_000, 10_000, 100_000)


def only_a_strings(strings):
    """Código fornecido, sem alterações."""
    result = []
    for s in strings:
        if len(s) > 0 and s[0] == "a":
            result.append(s)
    return result


def only_a_strings_medida(strings):
    """Mesma estrutura. Devolve (resultado, voltas do laço, operações O(1) executadas)."""
    result, iteracoes, operacoes = [], 0, 0
    for s in strings:
        iteracoes += 1
        operacoes += 1                  # len(s) > 0
        if len(s) > 0:
            operacoes += 1              # s[0] == "a", só avaliado se a string não é vazia
            if s[0] == "a":
                operacoes += 1          # append
                result.append(s)
    return result, iteracoes, operacoes


def mostrar_exemplo():
    titulo("Exercício 7: only_a_strings: o laço executa uma vez por elemento")
    exemplo = ["abacate", "banana", "", "amora", "Ameixa", "acerola", "uva"]
    print(f"entrada: {exemplo}")
    print(f"saída:   {only_a_strings(exemplo)}")
    mesmo_resultado = only_a_strings(exemplo) == only_a_strings_medida(exemplo)[0]
    ok(mesmo_resultado, "cópia instrumentada devolve o mesmo resultado")


def mostrar_custo_por_tamanho():
    titulo("Iterações e operações O(1) em função de N")
    linhas = []
    for n in TAMANHOS:
        _, iteracoes, operacoes = only_a_strings_medida([random.choice(PALAVRAS) for _ in range(n)])
        _, _, pior = only_a_strings_medida(["a"] * n)     # pior caso: as 3 operações em toda volta
        linhas.append([milhar(n), milhar(iteracoes), milhar(operacoes), milhar(pior), f"{pior // n}·N"])
    tabela(["N", "iterações", "operações (aleatória)", "operações (pior caso)", "pior/N"], linhas)
    print("iterações = N em qualquer entrada; operações <= 3N  ->  T(N) = O(N)")


def main():
    random.seed(SEMENTE)
    mostrar_exemplo()
    print()
    mostrar_custo_por_tamanho()


if __name__ == "__main__":
    main()

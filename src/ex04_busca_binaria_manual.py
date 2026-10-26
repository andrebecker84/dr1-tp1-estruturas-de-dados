"""Exercício 4: busca binária passo a passo por 8 no mesmo array do Exercício 3.

Cada passo olha o elemento do meio do intervalo e decide: achou, vai para a esquerda ou vai para a
direita. Conta como 1 passo, como nos slides da Aula 2.
"""
import math

from algoritmos.busca import busca_binaria, busca_linear
from algoritmos.metricas import medir
from apresentacao.terminal import milhar, ok, tabela, titulo
from dados import ARRAY_DA_AULA_2

ALVO = 8
AUSENTE = 7
TAMANHOS = (7, 100, 1_000, 1_000_000)


def passos_da_binaria(seq, alvo):
    """Devolve (índice, passos, rastro), com rastro = [(início, fim, meio), ...]."""
    rastro = []
    indice, metricas = medir(busca_binaria, seq, alvo, ao_inspecionar=lambda *passo: rastro.append(passo))
    return indice, metricas.iteracoes, rastro


def decisao(valor, alvo):
    if valor == alvo:
        return "achou"
    return "descarta a direita" if alvo < valor else "descarta a esquerda"


def mostrar_rastro():
    titulo(f"Exercício 4: busca binária por {ALVO} em {list(ARRAY_DA_AULA_2)}  (N = {len(ARRAY_DA_AULA_2)})")
    indice, passos, rastro = passos_da_binaria(ARRAY_DA_AULA_2, ALVO)
    linhas = []
    for passo, (inicio, fim, meio) in enumerate(rastro, 1):
        valor = ARRAY_DA_AULA_2[meio]
        linhas.append([passo, f"[{inicio}..{fim}]", meio, valor, decisao(valor, ALVO)])
    tabela(["passo", "intervalo", "meio", "valor", "decisão"], linhas, ">^>><")
    print(f"\nencontrado no índice {indice} após {passos} comparação(ões)")
    ok(passos == 1, "8 é exatamente o elemento central: 1 comparação")


def mostrar_linear_x_binaria():
    titulo("Linear x binária para cada alvo possível")
    linhas = []
    for alvo in (*ARRAY_DA_AULA_2, AUSENTE):
        linear = medir(busca_linear, ARRAY_DA_AULA_2, alvo)[1].comparacoes
        linhas.append([alvo, linear, passos_da_binaria(ARRAY_DA_AULA_2, alvo)[1]])
    tabela(["alvo", "linear", "binária"], linhas)

    pior_teorico = math.floor(math.log2(len(ARRAY_DA_AULA_2))) + 1
    print(f"pior caso: linear = N = {len(ARRAY_DA_AULA_2)}; binária = int(log2 N) + 1 = {pior_teorico}")
    ok(max(linha[2] for linha in linhas) == pior_teorico, "pior caso da binária confere com log2 N")


def mostrar_pior_caso_por_tamanho():
    titulo("Pior caso com N crescente (alvo ausente, maior que todos)")
    linhas = [[milhar(n), milhar(n), passos_da_binaria(range(n), n)[1]] for n in TAMANHOS]
    tabela(["N", "linear O(N)", "binária O(log N)"], linhas)


def main():
    mostrar_rastro()
    print()
    mostrar_linear_x_binaria()
    print()
    mostrar_pior_caso_por_tamanho()


if __name__ == "__main__":
    main()

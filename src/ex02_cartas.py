"""Exercício 2: ordenação das 13 cartas de espadas trocando só cartas vizinhas.

Restrições adotadas: as cartas ficam em fila, viradas para cima; só se seguram duas cartas vizinhas
por vez, uma em cada mão; o único movimento é trocá-las de lugar; não há espaço extra na mesa.
Esse procedimento é o Bubble Sort com parada antecipada.
"""
import random

from algoritmos.ordenacao import bubble_sort_com_parada
from apresentacao.terminal import ok, tabela, titulo
from dados import SEMENTE

CARTAS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
VALOR = {carta: posicao for posicao, carta in enumerate(CARTAS, 1)}     # A=1 ... K=13


def ordenar_registrando(fila):
    """Ordena a fila e devolve, para cada passagem, (fila, comparações e trocas acumuladas)."""
    historico = []

    def registrar(lista, metricas):
        historico.append((lista[:], metricas.comparacoes, metricas.trocas))

    bubble_sort_com_parada(fila, chave=VALOR.get, ao_fim_da_passagem=registrar)
    return historico


def em_texto(fila):
    return " ".join(f"{carta:>2}" for carta in fila)


def mostrar_simulacao(inicial):
    titulo("Exercício 2: 13 cartas de espadas, só trocas entre vizinhas")
    print("estado inicial:", em_texto(inicial), "\n")
    historico = ordenar_registrando(inicial)

    linhas, antes = [], (0, 0)
    for passagem, (fila, comparacoes, trocas) in enumerate(historico, 1):
        linhas.append([passagem, em_texto(fila), comparacoes - antes[0], trocas - antes[1]])
        antes = (comparacoes, trocas)
    tabela(["passagem", "fila após a passagem", "comparações", "trocas"], linhas, "><>>")

    final, comparacoes, trocas = historico[-1]
    print("\nestado final:  ", em_texto(final))
    print(f"total: {len(historico)} passagens, {comparacoes} comparações, {trocas} trocas")
    ok(tuple(final) == CARTAS, "fila em ordem crescente A..K")


def mostrar_casos_extremos():
    titulo("Custo nos cenários extremos (N = 13)")
    linhas = []
    for nome, fila in [("já ordenada (melhor caso)", CARTAS), ("ordem inversa (pior caso)", CARTAS[::-1])]:
        historico = ordenar_registrando(fila)
        _, comparacoes, trocas = historico[-1]
        linhas.append([nome, len(historico), comparacoes, trocas])
    tabela(["cenário", "passagens", "comparações", "trocas"], linhas)


def main():
    random.seed(SEMENTE)
    inicial = list(CARTAS)
    random.shuffle(inicial)
    mostrar_simulacao(inicial)
    print()
    mostrar_casos_extremos()


if __name__ == "__main__":
    main()

"""Exercício 12: Bubble Sort com parada antecipada, sobre os mesmos dados do Exercício 11."""
from algoritmos.metricas import medir
from algoritmos.ordenacao import bubble_sort, bubble_sort_com_parada
from apresentacao.terminal import milhar, ok, tabela, titulo
from dados import TAMANHOS_DO_BUBBLE, Cenario, lista_no_cenario


def ganho(antes, depois):
    return f"{100 * (antes - depois) / antes:.1f}%"


def comparar(n, cenario):
    """Roda as duas versões na mesma entrada. Devolve (linha da tabela, se dão a mesma saída e trocas)."""
    entrada = lista_no_cenario(n, cenario)
    saida_classico, classico = medir(bubble_sort, entrada)
    saida_otimizado, otimizado = medir(bubble_sort_com_parada, entrada)
    concordam = saida_classico == saida_otimizado and classico.trocas == otimizado.trocas

    antes, depois = classico.comparacoes, otimizado.comparacoes
    contagens = [milhar(antes), milhar(depois), ganho(antes, depois), milhar(otimizado.trocas)]
    return [milhar(n), cenario, *contagens, f"{otimizado.passagens}/{n - 1}"], concordam


def main():
    titulo("Exercício 12: clássico x otimizado (mesmos dados do Exercício 11)")
    resultados = [comparar(n, cenario) for n in TAMANHOS_DO_BUBBLE for cenario in Cenario]
    linhas = [linha for linha, _ in resultados]
    tabela(["N", "cenário", "comp. clássico", "comp. otimizado", "ganho", "trocas (ambos)", "passagens"], linhas)
    ok(all(concordam for _, concordam in resultados), "mesma saída e mesmo número de trocas nas duas versões")
    print("\nordenada: N-1 comparações (1 passagem) -> melhor caso O(N)")
    print("inversa:  N(N-1)/2 comparações, sem ganho -> pior caso continua O(N²)")


if __name__ == "__main__":
    main()

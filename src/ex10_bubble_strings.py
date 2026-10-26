"""Exercício 10: Bubble Sort para strings.

É o mesmo bubble_sort do Exercício 9; só muda a chave de comparação. Sem chave, vale a ordem
lexicográfica do Python (código Unicode); com chave_alfabetica, a ordem de dicionário.
"""
from algoritmos.ordenacao import bubble_sort, identidade
from algoritmos.texto import chave_alfabetica
from apresentacao.terminal import ok, titulo
from verificacao import ordenacao_correta

FRUTAS = ["uva", "banana", "abacate", "manga", "caju", "laranja"]
PREFIXOS = ["casamento", "casa", "cas", "casarão", "caso"]
MAIUSCULAS = ["banana", "Zebra", "abacate", "Maçã"]
ACENTOS = ["ética", "ervilha", "zebra", "ábaco", "abelha"]
NUMEROS_COMO_TEXTO = ["10", "9", "100", "2", "1"]

CASOS = (
    ("1) minúsculas sem acento", FRUTAS, identidade),
    ("2) prefixos: o menor prefixo vem antes", PREFIXOS, identidade),
    ("3) maiúsculas/minúsculas, ordem lexicográfica pura (código Unicode)", MAIUSCULAS, identidade),
    ("4) mesmo conjunto com chave_alfabetica, ordem de dicionário", MAIUSCULAS, chave_alfabetica),
    ("5) acentos, ordem lexicográfica pura", ACENTOS, identidade),
    ("6) acentos com chave_alfabetica", ACENTOS, chave_alfabetica),
    ("7) números como texto: comparação dígito a dígito", NUMEROS_COMO_TEXTO, identidade),
)


def ordenar_e_mostrar(nome, palavras, chave):
    """Ordena, imprime entrada e saída e devolve se a saída está correta."""
    saida = bubble_sort(palavras, chave=chave)
    print(f"{nome}\n  entrada: {palavras}\n  saída:   {saida}")
    return ordenacao_correta(palavras, saida, chave)


def main():
    titulo("Exercício 10: Bubble Sort para strings")
    corretas = [ordenar_e_mostrar(*caso) for caso in CASOS]
    print()
    ok(all(corretas), "todas as saídas ordenadas sob o critério usado e com as mesmas palavras")
    print(f"códigos: 'Z'={ord('Z')} < 'a'={ord('a')} < 'z'={ord('z')} < 'á'={ord('á')}")


if __name__ == "__main__":
    main()

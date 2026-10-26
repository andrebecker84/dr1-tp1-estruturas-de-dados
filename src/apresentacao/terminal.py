"""Saída no terminal: títulos, tabelas e o resultado das verificações."""
import sys

COLORIDO = sys.stdout.isatty()      # redirecionada para arquivo, a saída sai sem cores


def _cor(codigo, texto):
    return f"\033[{codigo}m{texto}\033[0m" if COLORIDO else texto


def titulo(texto):
    print(_cor("1;36", texto))
    print(_cor("2", "─" * len(texto)))


def ok(condicao, descricao):
    """Imprime [OK] ou [FALHA] com a descrição."""
    marca = _cor("1;32", "[OK]") if condicao else _cor("1;31", "[FALHA]")
    print(f"{marca} {descricao}")


def tabela(cabecalho, linhas, alinhamento=None):
    """Tabela com colunas alinhadas; alinhamento tem '<' ou '>' por coluna (padrão: só a 1ª à esquerda)."""
    linhas = [[str(celula) for celula in linha] for linha in linhas]
    larguras = [max(len(str(celula)) for celula in coluna) for coluna in zip(cabecalho, *linhas)]
    alinhamento = alinhamento or "<" + ">" * (len(cabecalho) - 1)

    def formatar(linha):
        return "  ".join(f"{celula:{a}{w}}" for celula, a, w in zip(linha, alinhamento, larguras))

    print(_cor("1", formatar([str(c) for c in cabecalho])))
    print("  ".join("─" * w for w in larguras))
    for linha in linhas:
        print(formatar(linha))


def compacta(lista):
    """Lista sem vírgulas, para caber no terminal: [3, 1, 2] -> [3 1 2]."""
    return "[" + " ".join(str(x) for x in lista) + "]"


def milhar(n):
    """Separador de milhar brasileiro: 1234567 -> 1.234.567."""
    return f"{n:,}".replace(",", ".")

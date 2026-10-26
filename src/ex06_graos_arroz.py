"""Exercício 6: menor quadrado do tabuleiro com pelo menos qtd_graos grãos."""
from algoritmos.metricas import medir
from algoritmos.tabuleiro import MAX_POR_QUADRADO, MENSAGEM_LIMITE, TOTAL_DO_TABULEIRO, menor_quadrado
from apresentacao.terminal import milhar, ok, tabela, titulo

# (faixa, qtd_graos, quadrado esperado)
TESTES = (
    ("pequeno", 1, 1), ("pequeno", 2, 2), ("pequeno", 4, 3), ("pequeno", 8, 4), ("pequeno", 5, 4),
    ("intermediário", 1_000, 11), ("intermediário", 1_000_000, 21),
    ("limite", MAX_POR_QUADRADO, 64),
    ("acima do quadrado 64", MAX_POR_QUADRADO + 1, MENSAGEM_LIMITE),
    ("acima do total", TOTAL_DO_TABULEIRO + 1, MENSAGEM_LIMITE),
)


def mostrar_testes():
    titulo("Exercício 6: menor quadrado com grãos >= qtd_graos")
    linhas, todos_ok = [], True
    for faixa, qtd, esperado in TESTES:
        quadrado, metricas = medir(menor_quadrado, qtd)
        todos_ok = todos_ok and quadrado == esperado
        exibido = "mensagem" if quadrado == MENSAGEM_LIMITE else quadrado
        linhas.append([faixa, milhar(qtd), exibido, metricas.iteracoes])
    tabela(["faixa", "qtd_graos", "quadrado", "iterações"], linhas)
    ok(todos_ok, "todos os resultados conferem com o esperado")


def mostrar_limites():
    acima_do_total = TOTAL_DO_TABULEIRO + 1
    print(f"\nmensagem para {milhar(acima_do_total)} grãos:")
    print(f"  {menor_quadrado(acima_do_total)} (máximo de {milhar(MAX_POR_QUADRADO)} grãos, no quadrado 64)")
    print(f"total do tabuleiro: {milhar(TOTAL_DO_TABULEIRO)} grãos (2^64 - 1)")
    try:
        menor_quadrado(0)
        ok(False, "entrada inválida (0) deveria gerar ValueError")
    except ValueError as erro:
        ok(True, f"entrada inválida rejeitada: {erro}")


def main():
    mostrar_testes()
    mostrar_limites()


if __name__ == "__main__":
    main()

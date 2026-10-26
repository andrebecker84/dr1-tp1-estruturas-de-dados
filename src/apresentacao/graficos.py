"""Estilo dos gráficos do notebook (matplotlib).

Só o notebook usa este arquivo; os scripts dos exercícios continuam só com a biblioteca padrão.
Cada gráfico também é salvo em evidencias/graficos/ para aparecer no README e no docs/tp1.md.
"""
import os

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

AZUL, LARANJA, VERDE = "#2a78d6", "#eb6834", "#1baf7a"
TEXTO, TEXTO_2, GRADE, FUNDO = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
PASTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "evidencias", "graficos")


def novo(titulo, eixo_x, eixo_y):
    """Figura com um eixo só, grade discreta e sem bordas de cima e da direita."""
    fig, ax = plt.subplots(figsize=(7.5, 3.8), dpi=110)
    fig.patch.set_facecolor(FUNDO)
    ax.set_facecolor(FUNDO)
    ax.set_title(titulo, loc="left", fontsize=12, color=TEXTO, pad=12)
    ax.set_xlabel(eixo_x, color=TEXTO_2)
    ax.set_ylabel(eixo_y, color=TEXTO_2)
    ax.grid(True, color=GRADE, linewidth=0.8)
    ax.set_axisbelow(True)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    for lado in ("left", "bottom"):
        ax.spines[lado].set_color(GRADE)
    ax.tick_params(colors=TEXTO_2, labelsize=9)
    return fig, ax


def linha(ax, x, y, cor, rotulo):
    marcador = "o" if len(x) <= 21 else None      # numa série densa os marcadores viram uma faixa
    ax.plot(x, y, color=cor, linewidth=2, label=rotulo, marker=marcador, markersize=4)


def milhares(ax):
    """Eixo y com separador de milhar no padrão brasileiro (500.000)."""
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:,.0f}".replace(",", ".")))


def mostrar(fig, ax, nome, **legenda):
    """Legenda, salva o PNG e exibe no notebook."""
    ax.legend(frameon=False, labelcolor=TEXTO_2, **legenda)
    fig.tight_layout()
    os.makedirs(PASTA, exist_ok=True)
    fig.savefig(os.path.join(PASTA, nome + ".png"), facecolor=FUNDO)
    plt.show()

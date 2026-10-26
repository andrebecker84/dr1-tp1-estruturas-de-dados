# -*- coding: utf-8 -*-
"""Converte as capturas do tmux (texto com cores ANSI) em imagens PNG de terminal.

    python scripts/renderizar_telas.py

Le evidencias/telas/ansi/NN-nome.ans, gravados por `tmux capture-pane -e -p` em
scripts/capturar_telas.sh, e grava evidencias/telas/NN-nome.png. O conteudo e exatamente o
buffer da tela do terminal no momento da captura: comandos, saidas, cores e o paginador less.
Nada e redigitado - o script so desenha o que o tmux devolveu.
"""
import glob, os, re
from PIL import Image, ImageDraw, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEM = os.path.join(RAIZ, 'evidencias', 'telas', 'ansi')
DESTINO = os.path.join(RAIZ, 'evidencias', 'telas')

FONTE, TAM = r'C:\Windows\Fonts\consola.ttf', 26
FONTE_B = r'C:\Windows\Fonts\consolab.ttf'
COLUNAS = 110           # largura do painel do tmux
PAD, BARRA = 28, 54     # margem interna e altura da barra de titulo

FUNDO, TEXTO = (30, 30, 36), (220, 220, 220)
# Paleta ANSI do Ubuntu (gnome-terminal), indices 0-15.
PALETA = [(46, 52, 54), (204, 0, 0), (78, 154, 6), (196, 160, 0), (52, 101, 164),
          (117, 80, 123), (6, 152, 154), (211, 215, 207), (85, 87, 83), (239, 41, 41),
          (138, 226, 52), (252, 233, 79), (114, 159, 207), (173, 127, 168), (52, 226, 226),
          (238, 238, 236)]


def cor256(n):
    if n < 16:
        return PALETA[n]
    if n < 232:
        n -= 16
        niv = [0, 95, 135, 175, 215, 255]
        return niv[n // 36], niv[(n // 6) % 6], niv[n % 6]
    v = 8 + (n - 232) * 10
    return v, v, v


def celulas(linha):
    """Quebra uma linha com SGR em [(caractere, frente, fundo, negrito)]."""
    fg, bg, neg, inv = None, None, False, False
    saida = []
    for parte in re.split(r'(\x1b\[[0-9;:]*m)', linha):
        if not parte.startswith('\x1b['):
            for ch in parte.replace('\t', '        '):
                f, b = (bg or FUNDO, fg or TEXTO) if inv else (fg, bg)
                saida.append((ch, f, b, neg))
            continue
        cods = [int(c) if c.isdigit() else 0 for c in re.split('[;:]', parte[2:-1])] or [0]
        i = 0
        while i < len(cods):
            c = cods[i]
            if c == 0:
                fg, bg, neg, inv = None, None, False, False
            elif c == 1:
                neg = True
            elif c == 22:
                neg = False
            elif c == 7:
                inv = True
            elif c == 27:
                inv = False
            elif 30 <= c <= 37:
                fg = PALETA[c - 30 + (8 if neg else 0)]
            elif 90 <= c <= 97:
                fg = PALETA[c - 90 + 8]
            elif 40 <= c <= 47:
                bg = PALETA[c - 40]
            elif 100 <= c <= 107:
                bg = PALETA[c - 100 + 8]
            elif c == 39:
                fg = None
            elif c == 49:
                bg = None
            elif c in (38, 48) and i + 1 < len(cods):
                if cods[i + 1] == 5 and i + 2 < len(cods):
                    rgb = cor256(cods[i + 2]); i += 2
                elif cods[i + 1] == 2 and i + 4 < len(cods):
                    rgb = tuple(cods[i + 2:i + 5]); i += 4
                else:
                    rgb = None
                if c == 38:
                    fg = rgb
                else:
                    bg = rgb
            i += 1
    return saida


def renderiza(origem, destino, titulo):
    linhas = open(origem, encoding='utf-8', errors='replace').read().split('\n')
    while linhas and not re.sub(r'\x1b\[[0-9;:]*m', '', linhas[-1]).strip():
        linhas.pop()
    fonte = ImageFont.truetype(FONTE, TAM)
    fonte_b = ImageFont.truetype(FONTE_B, TAM)
    larg_c = fonte.getlength('M')
    alt_l = int(TAM * 1.32)
    w = int(PAD * 2 + larg_c * COLUNAS)
    h = BARRA + PAD * 2 + alt_l * max(len(linhas), 3)
    img = Image.new('RGB', (w, h), FUNDO)
    g = ImageDraw.Draw(img)

    # Barra de titulo no estilo do Windows Terminal, com o titulo da sessao.
    g.rectangle([0, 0, w, BARRA], fill=(44, 44, 52))
    for k, cor in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        cx = PAD + k * 34
        g.ellipse([cx, BARRA // 2 - 9, cx + 18, BARRA // 2 + 9], fill=cor)
    ft = ImageFont.truetype(FONTE, 22)
    g.text((w / 2, BARRA / 2), titulo, font=ft, fill=(190, 190, 196), anchor='mm')

    y = BARRA + PAD
    for linha in linhas:
        x = PAD
        for ch, fg, bg, neg in celulas(linha):
            if bg:
                g.rectangle([x, y, x + larg_c, y + alt_l], fill=bg)
            if ch != ' ':
                g.text((x, y + 3), ch, font=fonte_b if neg else fonte, fill=fg or TEXTO)
            x += larg_c
        y += alt_l
    img.save(destino, optimize=True)


if __name__ == '__main__':
    arquivos = sorted(glob.glob(os.path.join(ORIGEM, '*.ans')))
    for a in arquivos:
        nome = os.path.splitext(os.path.basename(a))[0]
        renderiza(a, os.path.join(DESTINO, nome + '.png'),
                  'becker@alienwarePC: Ubuntu 24.04 (WSL2) - bash')
    print('telas renderizadas: %d' % len(arquivos))

# -*- coding: utf-8 -*-
"""Monta e executa o notebook DR1_TP1.ipynb a partir de docs/RELATORIO_TP1.md.

    uv run --no-project --python 3.12 --with nbformat --with nbclient --with ipykernel --with matplotlib python scripts/gerar-notebook.py

Cada exercicio vira: enunciado, teoria, codigo (o trecho com as funcoes principais), a execucao do
script do exercicio, os graficos e a resposta. Como reconhece cada parte do docs/RELATORIO_TP1.md:
  <!-- codigo: ... -->     o bloco ```python dentro dele vira celula de codigo
  <!-- executa: MODULO --> celula que roda MODULO.main(), com a saida gravada no notebook
  <!-- notebook ... -->    celula de codigo que so existe no notebook (graficos, testes)
  ```python               celula de codigo
  ![Figura ...] e ![Grafico ...]   ignorados: aqui a saida e o grafico aparecem ao vivo
  outros comentarios HTML          ignorados
Os graficos sao salvos em evidencias/graficos/ ao executar (src/graficos.py).
"""
import os, re

import nbformat
from nbclient import NotebookClient

from tp1_fonte import RAIZ, contexto, para_geradores, sincronizar

SAIDA = os.path.join(RAIZ, 'DR1_TP1.ipynb')
REPOSITORIO = 'https://github.com/andrebecker84/dr1-tp1-estruturas-de-dados'

# Capa do notebook, no mesmo padrão visual do README.
CAPA = f"""<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1E3A8A,100:2A78D6&height=180&section=header&text=Busca%2C%20Ordena%C3%A7%C3%A3o%20e%20Big%20O&fontSize=46&fontColor=ffffff&fontAlignY=36&desc=DR1-TP1%20%C2%B7%20notebook&descAlignY=58&descSize=17" width="100%" />

# 🔎 Busca, Ordenação e Big O

**Velocidade e Qualidade com Estruturas de Dados e Algoritmos · DR1-TP1**

<img src="https://img.shields.io/badge/Python-3.15.2-3776AB?style=flat-square&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/depend%C3%AAncias-s%C3%B3%20biblioteca%20padr%C3%A3o-3776AB?style=flat-square&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/unittest-19%20passando-1BAF7A?style=flat-square" />
<img src="https://img.shields.io/badge/license-source%20available-8957e5?style=flat-square" />

</div>

| | |
|---|---|
| **Aluno** | André Luis Becker |
| **Professor** | Ian Monteiro Nunes |
| **Disciplina** | Velocidade e Qualidade com Estruturas de Dados e Algoritmos |
| **Bloco · Trimestre** | Ciência da Computação · 26E4 |
| **Repositório** | [{REPOSITORIO.split('github.com/')[1]}]({REPOSITORIO}) |

Para cada exercício: o **enunciado**, a **teoria** das aulas, o **código** com a execução, os
**gráficos** quando ajudam a ver o crescimento, e a minha **resposta**."""


def montar(texto):
    texto = texto[texto.index('\n## '):]        # o cabeçalho do relatório dá lugar à capa
    celulas, md = [nbformat.v4.new_markdown_cell(CAPA)], []

    def codigo(fonte):
        celulas.append(nbformat.v4.new_code_cell(fonte.strip('\n')))

    def fecha_md():
        bloco = '\n'.join(md).strip('\n')
        if bloco:
            celulas.append(nbformat.v4.new_markdown_cell(bloco))
        md.clear()

    linhas = texto.split('\n')
    i = 0
    while i < len(linhas):
        l = linhas[i]
        if l.startswith('<!-- notebook'):
            fecha_md()
            corpo = []
            i += 1
            while linhas[i].strip() != '-->':
                corpo.append(linhas[i])
                i += 1
            codigo('\n'.join(corpo))
        elif l.startswith('<!-- executa:'):
            fecha_md()
            modulo = l.split(':', 1)[1].replace('-->', '').strip()
            codigo('import %s\n%s.main()' % (modulo, modulo))
        elif l.startswith('<!-- codigo:'):
            fecha_md()
            # O trecho vem sem os imports e as constantes do arquivo; sem eles a celula nao roda sozinha.
            arquivo = l.split(':', 1)[1].replace('-->', '').split()[0]
            corpo = ["# src/%s" % arquivo, *contexto(arquivo), "", ""]
            while not linhas[i].startswith('```python'):
                i += 1
            i += 1
            while not linhas[i].startswith('```'):
                corpo.append(linhas[i])
                i += 1
            codigo('\n'.join(corpo))
            while not linhas[i].startswith('<!-- /codigo'):
                i += 1
        elif l.startswith('```python'):
            fecha_md()
            corpo = []
            i += 1
            while not linhas[i].startswith('```'):
                corpo.append(linhas[i])
                i += 1
            codigo('\n'.join(corpo))
        elif l.startswith('<!--'):
            while '-->' not in linhas[i]:
                i += 1
        elif re.match(r'^!\[(Figura|Gráfico)', l):
            pass
        else:
            if l.startswith('## ') or l.startswith('### '):
                fecha_md()
            md.append(l)
        i += 1
    fecha_md()

    nb = nbformat.v4.new_notebook(cells=celulas)
    nb.metadata['kernelspec'] = {'name': 'python3', 'display_name': 'Python 3', 'language': 'python'}
    nb.metadata['language_info'] = {'name': 'python'}
    return nb


if __name__ == '__main__':
    nb = montar(para_geradores(sincronizar()))
    NotebookClient(nb, timeout=900, kernel_name='python3',
                   resources={'metadata': {'path': RAIZ}}).execute()
    nbformat.write(nb, SAIDA)
    n_codigo = sum(1 for c in nb.cells if c.cell_type == 'code')
    print('gerado: %s | celulas: %d (%d de codigo)' % (SAIDA, len(nb.cells), n_codigo))

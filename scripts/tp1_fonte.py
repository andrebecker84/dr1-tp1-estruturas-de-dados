# -*- coding: utf-8 -*-
"""Preenche os blocos automaticos de docs/tp1.md a partir de src/.

    python scripts/tp1_fonte.py

O docs/tp1.md e lido direto no GitHub, entao o codigo e a conclusao do Exercicio 13 precisam estar
escritos nele. Para nao copiar a mao (e desatualizar), cada bloco marcado com comentario HTML e
regerado aqui:

  <!-- codigo: ARQUIVO f,g -->   ...   <!-- /codigo -->   funcoes f e g de src/ARQUIVO, sem docstring
  <!-- inclui: ARQUIVO -->       ...   <!-- /inclui -->   markdown de src/ARQUIVO, secoes rebaixadas
  <!-- video: URL -->            ...   <!-- /video -->    linha com o link do video (ou "a inserir")

Os dois geradores (notebook e PDF) chamam sincronizar() antes de ler o arquivo.
"""
import ast, io, os, re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(RAIZ, 'src')
TP1 = os.path.join(RAIZ, 'docs', 'tp1.md')

BLOCO = re.compile(r'<!-- (codigo|inclui|video):[ \t]*(.*?) -->\n.*?<!-- /\1 -->', re.S)


def trecho(arquivo, nomes):
    """Linhas das funcoes e classes pedidas de src/<arquivo>, na ordem do arquivo, sem docstrings."""
    texto = io.open(os.path.join(SRC, arquivo), encoding='utf-8').read()
    linhas = texto.split('\n')
    saida = []
    for n in ast.parse(texto).body:
        if not (isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in nomes):
            continue
        doc = n.body[0] if (isinstance(n.body[0], ast.Expr)
                            and isinstance(n.body[0].value, ast.Constant)) else None
        corpo = [l for k, l in enumerate(linhas[n.lineno - 1:n.end_lineno], n.lineno)
                 if not (doc and doc.lineno <= k <= doc.end_lineno)]
        saida += ([''] if saida else []) + corpo
    return saida


def contexto(arquivo):
    """Imports e constantes de src/<arquivo>: o notebook os poe antes do trecho para ele rodar sozinho."""
    texto = io.open(os.path.join(SRC, arquivo), encoding='utf-8').read()
    linhas = texto.split('\n')
    topo = (ast.Import, ast.ImportFrom, ast.Assign)
    return ['\n'.join(linhas[n.lineno - 1:n.end_lineno]) for n in ast.parse(texto).body if isinstance(n, topo)]


def _conteudo(tipo, args):
    if tipo == 'codigo':
        arquivo, funcoes = args.split()
        return '```python\n%s\n```\n' % '\n'.join(trecho(arquivo, funcoes.split(',')))
    if tipo == 'inclui':
        md = io.open(os.path.join(SRC, args), encoding='utf-8').read()
        md = re.sub(r'^# .*\n+', '', md)
        return re.sub(r'^## ', '#### ', md, flags=re.M).strip('\n') + '\n'
    if args:
        return '**Link do vídeo:** [assistir no Google Drive](%s)\n' % args
    return '**Link do vídeo:** a inserir.\n'


def sincronizar():
    texto = io.open(TP1, encoding='utf-8').read()

    def troca(m):
        tipo, args = m.group(1), m.group(2).strip()
        abre = '<!-- %s:%s -->' % (tipo, ' ' + args if args else '')
        return '%s\n%s<!-- /%s -->' % (abre, _conteudo(tipo, args), tipo)

    novo = BLOCO.sub(troca, texto)
    if novo != texto:
        io.open(TP1, 'w', encoding='utf-8', newline='\n').write(novo)
    return novo


if __name__ == '__main__':
    sincronizar()
    print('atualizado: %s' % TP1)

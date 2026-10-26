#!/usr/bin/env bash
# Executa os 14 exercicios do DR1-TP1 num terminal real (bash dentro de um tmux, no Ubuntu do WSL)
# e captura cada tela.
#
#     wsl -d Ubuntu --exec bash scripts/capturar_telas.sh
#
# O codigo de src/ e copiado para ~/DR1_TP1 e cada comando e digitado no terminal como um usuario
# faria (tmux send-keys). As telas saem de `tmux capture-pane -e` (o buffer do terminal, com cores,
# desde o ultimo clear) e viram PNG em renderizar_telas.py. A saida de cada exercicio tambem e
# gravada, sem cores, em evidencias/saidas/exNN.txt.
set -u

RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
ANSI="$RAIZ/evidencias/telas/ansi"
SAIDAS="$RAIZ/evidencias/saidas"
W="$HOME/DR1_TP1"
S=tp1
T=(tmux -L tp1 -f "$RAIZ/scripts/tmux_tp1.conf")
FIG=0

# ------------------------------------------------------------------ estado limpo
"${T[@]}" kill-server 2>/dev/null
rm -rf "$W"
mkdir -p "$W" "$ANSI" "$SAIDAS"
cp -r "$RAIZ"/src/. "$W"/
find "$W" -name __pycache__ -prune -exec rm -rf {} +
# Vindos de /mnt/c, os arquivos chegariam com permissao de execucao.
find "$W" -type d -exec chmod 755 {} + && find "$W" -type f -exec chmod 644 {} +
rm -f "$ANSI"/*.ans "$RAIZ"/evidencias/telas/*.png "$SAIDAS"/*.txt

"${T[@]}" new-session -d -s $S -x 110 -y 45 -c "$W" "bash --rcfile '$RAIZ/scripts/bashrc_tp1' -i"

espera() { timeout 120 "${T[@]}" wait-for pronto || echo "AVISO: prompt nao voltou" >&2; }
digita() { "${T[@]}" send-keys -t $S -l -- "$1"; "${T[@]}" send-keys -t $S Enter; }
cmd()    { digita "$1"; espera; }
limpa()  { cmd clear; "${T[@]}" clear-history -t $S; }

# Captura tudo desde o ultimo clear (historico + area visivel): saidas longas nao sao cortadas.
tela() {
    FIG=$((FIG + 1))
    "${T[@]}" capture-pane -t $S -e -p -S - -E - > "$ANSI/$(printf '%02d-%s' "$FIG" "$1").ans"
}

# executa NOME "comando" ["comando" ...]: limpa a tela, digita os comandos e captura.
executa() {
    local nome="$1"; shift
    limpa
    for c in "$@"; do cmd "$c"; done
    tela "$nome"
}

espera   # primeiro prompt

executa ex01-busca-linear          "python3 ex01_busca_linear.py"
executa ex02-cartas                "python3 ex02_cartas.py"
executa ex03-busca-linear-manual   "python3 ex03_busca_linear_manual.py"
executa ex04-busca-binaria-manual  "python3 ex04_busca_binaria_manual.py"
executa ex05-maior-unico           "python3 ex05_maior_unico.py"
executa ex06-graos-arroz           "python3 ex06_graos_arroz.py"
executa ex07-only-a-strings        "python3 ex07_only_a_strings.py"
executa ex08-cocktail-sort         "python3 ex08_cocktail_sort.py"
executa ex09-bubble-sort           "python3 ex09_bubble_sort.py"
executa ex10-bubble-strings        "python3 ex10_bubble_strings.py"
executa ex11-bubble-instrumentado  "python3 ex11_bubble_instrumentado.py"
executa ex12-bubble-otimizado      "python3 ex12_bubble_otimizado.py"
executa ex13-comparacao-buscas     "python3 ex13_comparacao_buscas.py"
executa ex14-refatoracao-teste     "python3 ex14_refatoracao.py" \
                                   "python3 -m unittest -v tests.test_ex14_refatoracao" \
                                   "python3 -m unittest discover -s tests -t ."

"${T[@]}" kill-server

# ------------------------------------------------------- saidas em texto puro
cd "$W" || exit 1
for f in ex[0-9][0-9]_*.py; do
    PYTHONDONTWRITEBYTECODE=1 python3 "$f" > "$SAIDAS/${f%%_*}.txt" 2>&1
done
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -t . -v > "$SAIDAS/testes.txt" 2>&1
echo "telas capturadas: $FIG | saidas gravadas: $(ls "$SAIDAS" | wc -l)"

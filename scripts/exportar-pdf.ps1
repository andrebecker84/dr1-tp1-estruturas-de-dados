# Exporta andre_becker_DR1_TP1.docx para PDF pelo proprio Word (mesma renderizacao do arquivo aberto).
#
#     powershell -ExecutionPolicy Bypass -File scripts/exportar-pdf.ps1
$raiz = Split-Path -Parent $PSScriptRoot
$docx = Join-Path $raiz 'andre_becker_DR1_TP1.docx'
$pdf  = Join-Path $raiz 'andre_becker_DR1_TP1.pdf'

$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $doc = $word.Documents.Open($docx, $false, $true)   # sem conversao, somente leitura
    $doc.Fields.Update() | Out-Null
    $doc.ExportAsFixedFormat($pdf, 17)                  # 17 = wdExportFormatPDF
    $doc.Close($false)
} finally {
    $word.Quit()
}
"gerado: $pdf"

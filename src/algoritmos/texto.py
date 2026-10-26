"""Chave de ordenação alfabética para palavras em português (Exercício 10)."""
import unicodedata


def chave_alfabetica(palavra):
    """Palavra em minúsculas e sem acentos ('Ébano' -> 'ebano'), para ordenar como num dicionário."""
    decomposta = unicodedata.normalize("NFD", palavra.casefold())
    return "".join(letra for letra in decomposta if unicodedata.category(letra) != "Mn")

"""Módulo de layout usando Rich."""

from rich.console import Console
from rich.columns import Columns

console = Console()

def exibir_colunas(texto: str, isArquivo: bool):
    """Exibe o texto em colunas usando Rich."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    linhas = texto.splitlines()
    console.print(Columns(linhas))


def exibir_layout_simples(texto: str, isArquivo: bool):
    """Exibe o texto linha a linha com separadores."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    for linha in texto.splitlines():
        console.rule(linha)

"""Módulo de painel usando Rich."""

from rich.console import Console
from rich.panel import Panel

console = Console()

def painel_padrao(texto: str, isArquivo: bool):
    """Exibe texto em painel padrão."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    console.print(Panel(texto))


def painel_com_titulo(texto: str, isArquivo: bool):
    """Exibe texto com painel e título."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    console.print(Panel(texto, title="Painel Estilizado"))

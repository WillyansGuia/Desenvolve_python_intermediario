"""Módulo de estilo com cores e ênfase."""

from rich.console import Console
from rich.text import Text

console = Console()

def texto_colorido(texto: str, isArquivo: bool):
    """Texto com cores variadas."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    t = Text(texto, style="bold magenta")
    console.print(t)


def texto_com_estilo(texto: str, isArquivo: bool):
    """Texto sublinhado e em itálico."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    t = Text(texto)
    t.stylize("italic underline")
    console.print(t)

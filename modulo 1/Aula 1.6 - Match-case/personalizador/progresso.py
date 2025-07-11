"""Módulo de progresso usando Rich."""

from rich.progress import Progress
from time import sleep

def barra_progresso(texto: str, isArquivo: bool):
    """Simula uma barra de progresso."""
    with Progress() as progress:
        tarefa = progress.add_task("[green]Processando...", total=100)
        while not progress.finished:
            progress.update(tarefa, advance=10)
            sleep(0.3)


def progresso_personalizado(texto: str, isArquivo: bool):
    """Simula progresso personalizado com descrição."""
    descricao = texto
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            descricao = f.read()
    with Progress() as progress:
        task = progress.add_task(f"[cyan]{descricao}", total=50)
        while not progress.finished:
            progress.update(task, advance=5)
            sleep(0.2)

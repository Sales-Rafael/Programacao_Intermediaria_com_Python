"""
Módulo progresso.py

Este módulo contém funções para exibição de progresso utilizando a biblioteca rich.

Funções:
    - formatar1: Exibe um texto após uma barra de progresso simulada.
    - formatar2: Exibe um texto após um spinner de carregamento.
"""

from rich.console import Console
from rich.progress import Progress
import time

def formatar1(texto, isArquivo):
    """Simula uma barra de progresso enquanto exibe o texto."""
    console = Console()
    with Progress() as progress:
        tarefa = progress.add_task("[cyan]Processando...", total=100)
        for _ in range(10):
            time.sleep(0.2)
            progress.update(tarefa, advance=10)
    console.print(texto)

def formatar2(texto, isArquivo):
    """Exibe um spinner enquanto carrega o texto."""
    console = Console()
    with console.status("[bold green]Carregando...") as status:
        time.sleep(2)
    console.print(texto)

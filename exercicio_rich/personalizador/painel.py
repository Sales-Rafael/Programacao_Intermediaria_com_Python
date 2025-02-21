"""
Módulo painel.py

Este módulo contém funções para exibição de texto dentro de painéis formatados utilizando a biblioteca rich.

Funções:
    - formatar1: Exibe um texto dentro de um painel simples.
    - formatar2: Exibe um texto dentro de um painel destacado com borda colorida.
"""

from rich.console import Console
from rich.panel import Panel

def formatar1(texto, isArquivo):
    """Exibe o texto dentro de um painel simples."""
    console = Console()
    console.print(Panel(texto, title="Painel Simples"))

def formatar2(texto, isArquivo):
    """Exibe o texto dentro de um painel destacado."""
    console = Console()
    console.print(Panel(texto, title="Painel Destacado", border_style="bold magenta"))

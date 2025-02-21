"""
Módulo estilo.py

Este módulo contém funções para exibição de texto com diferentes estilos utilizando a biblioteca rich.

Funções:
    - formatar1: Exibe um texto com estilo em negrito e sublinhado.
    - formatar2: Exibe um texto colorido com gradiente de azul para verde.
"""

from rich.console import Console
from rich.text import Text

def formatar1(texto, isArquivo):
    """Exibe o texto com um estilo em negrito e sublinhado."""
    console = Console()
    text_obj = Text(texto, style="bold underline")
    console.print(text_obj)

def formatar2(texto, isArquivo):
    """Exibe o texto colorido com gradiente de azul para verde."""
    console = Console()
    text_obj = Text(texto)
    text_obj.stylize("bold cyan", 0, len(texto)//2)
    text_obj.stylize("bold green", len(texto)//2, len(texto))
    console.print(text_obj)

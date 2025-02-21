"""
Módulo layout.py

Este módulo contém funções para exibição de texto utilizando diferentes layouts da biblioteca rich.

Funções:
    - formatar1: Exibe um texto dentro de um layout básico com cabeçalho e rodapé.
    - formatar2: Exibe um texto centralizado dentro de um layout dividido em colunas.
"""

from rich.console import Console
from rich.layout import Layout

def formatar1(texto, isArquivo):
    """Formata o texto em um layout básico."""
    console = Console()
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body"),
        Layout(name="footer", size=3)
    )
    layout["header"].update("=== Cabeçalho ===")
    layout["body"].update(texto)
    layout["footer"].update("=== Rodapé ===")
    console.print(layout)

def formatar2(texto, isArquivo):
    """Exibe o texto dentro de um layout centralizado."""
    console = Console()
    layout = Layout()
    layout.split_row(
        Layout(name="left", size=20),
        Layout(name="center"),
        Layout(name="right", size=20)
    )
    layout["center"].update(texto)
    console.print(layout)

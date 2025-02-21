"""
Arquivo principal (main.py) para execução do programa.

Este script recebe argumentos da linha de comando e formata texto utilizando o pacote personalizador,
que inclui módulos para layout, painel, progresso e estilo.

Uso:
    python main.py "Texto aqui" -m layout -f formatar1
    python main.py caminho/para/arquivo.txt -a -m painel -f formatar2

Argumentos:
    texto ou caminho para arquivo
    -a, --arquivo: Indica que o argumento passado é um arquivo
    -m, --modulo: Define qual módulo será utilizado (layout, painel, progresso, estilo)
    -f, --funcao: Define a função dentro do módulo (formatar1, formatar2)
"""

import argparse
import os
from personalizador import layout, painel, progresso, estilo

def ler_arquivo(caminho):
    """Lê o conteúdo de um arquivo de texto."""
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    else:
        print("Arquivo não encontrado.")
        exit(1)

def main():
    parser = argparse.ArgumentParser(description="Programa que formata texto com a biblioteca rich.")
    parser.add_argument("texto", help="Texto a ser formatado ou caminho para o arquivo de texto.")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que o argumento 'texto' é um caminho para arquivo.")
    parser.add_argument("-m", "--modulo", choices=["layout", "painel", "progresso", "estilo"], required=True, help="Escolha o módulo de formatação.")
    parser.add_argument("-f", "--funcao", choices=["formatar1", "formatar2"], required=True, help="Escolha a função a ser utilizada dentro do módulo escolhido.")
    
    args = parser.parse_args()
    
    conteudo = ler_arquivo(args.texto) if args.arquivo else args.texto
    
    modulos = {"layout": layout, "painel": painel, "progresso": progresso, "estilo": estilo}
    modulo_selecionado = modulos[args.modulo]
    
    if hasattr(modulo_selecionado, args.funcao):
        funcao = getattr(modulo_selecionado, args.funcao)
        funcao(conteudo, args.arquivo)
    else:
        print("Função inválida para o módulo escolhido.")

if __name__ == "__main__":
    main()

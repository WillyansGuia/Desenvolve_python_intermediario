import argparse
from personalizador import layout, painel, progresso, estilo

modulos = {
    "layout": layout,
    "painel": painel,
    "progresso": progresso,
    "estilo": estilo
}

funcoes = {
    "layout": ["exibir_colunas", "exibir_layout_simples"],
    "painel": ["painel_padrao", "painel_com_titulo"],
    "progresso": ["barra_progresso", "progresso_personalizado"],
    "estilo": ["texto_colorido", "texto_com_estilo"]
}

parser = argparse.ArgumentParser(description="Exibe texto com formatação Rich.")
parser.add_argument("entrada", help="Texto a exibir ou caminho para o arquivo.")
parser.add_argument("-a", "--arquivo", action="store_true", help="Indica se a entrada é um caminho de arquivo.")
parser.add_argument("-m", "--modulo", required=True, choices=modulos.keys(), help=f"Módulo disponível: {list(modulos.keys())}")
parser.add_argument("-f", "--funcao", required=True, help="Função do módulo (veja o README para as opções).")

args = parser.parse_args()

modulo = modulos.get(args.modulo)
if not modulo:
    raise ValueError("Módulo inválido.")

if args.funcao not in funcoes[args.modulo]:
    raise ValueError(f"Função inválida para o módulo '{args.modulo}'. Use uma destas: {funcoes[args.modulo]}")

getattr(modulo, args.funcao)(args.entrada, args.arquivo)

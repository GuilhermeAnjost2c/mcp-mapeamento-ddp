"""
Configurações do servidor MCP para criação de apresentações DDP.
"""

import os

# Caminho para o template PowerPoint
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "DDP_TEMPLATE.pptx")

# Configurações padrão
DEFAULT_CONFIG = {
    "template_path": TEMPLATE_PATH,
    "default_layout_index": 1,  # Índice do layout padrão para novos slides
    "default_output_dir": "output",  # Diretório padrão para saída
    "file_prefix": "DDP_",  # Prefixo padrão para arquivos gerados
    "file_extension": ".pptx"  # Extensão dos arquivos gerados
}

# Placeholders suportados no template
PLACEHOLDERS = {
    "NOME_PROCESSO": "{Nome Processo}",
    "ETAPA": "{ETAPA}",
    "DESCRICAO": "{DESCRICAO}",
    "REGRAS": "{REGRAS}"
}

# Padrão regex para processamento de etapas
ETAPA_REGEX_PATTERN = r'# ETAPA (\d+) - (.+?)\nSupplier: (.+?)\nInput: (.+?)\nProcess: (.+?)\nOutput: (.+?)\nCustomer: (.+?)(?=\n#|$)'

def get_template_path():
    """Retorna o caminho do template."""
    return TEMPLATE_PATH

def get_default_config():
    """Retorna a configuração padrão."""
    return DEFAULT_CONFIG.copy()

def get_placeholders():
    """Retorna os placeholders suportados."""
    return PLACEHOLDERS.copy()

def get_etapa_regex():
    """Retorna o padrão regex para processamento de etapas."""
    return ETAPA_REGEX_PATTERN

def validate_template_exists():
    """Valida se o template existe."""
    return os.path.exists(TEMPLATE_PATH)

def get_output_directory(base_dir="output"):
    """Retorna o diretório de saída, criando se necessário."""
    if not os.path.exists(base_dir):
        os.makedirs(base_dir, exist_ok=True)
    return base_dir
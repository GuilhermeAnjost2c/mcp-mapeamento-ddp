# MCP Mapeamento - Gerador de DDP (Documento de Desenho de Processo)

Este é um servidor MCP (Model Context Protocol) que gera automaticamente apresentações PowerPoint para Documentos de Desenho de Processo (DDP) a partir de texto estruturado contendo as etapas de um processo.

## Funcionalidades

- **Geração automática de DDP**: Cria apresentações PowerPoint baseadas em templates pré-definidos
- **Processamento de etapas**: Extrai informações de texto estruturado seguindo um formato específico
- **Template personalizável**: Utiliza um template PowerPoint configurável
- **Nomes únicos de arquivo**: Evita sobrescrever arquivos existentes
- **Validação de arquivos**: Verifica se arquivos estão em uso antes de modificá-los

## Estrutura do Projeto

```
MCP/
├── server.py          # Servidor MCP principal
├── config.py          # Configurações do sistema
├── requirements.txt   # Dependências Python
├── mcp.json          # Configuração do servidor MCP
├── DDP_TEMPLATE.pptx # Template PowerPoint para DDP
└── README.md         # Este arquivo
```

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/GuilhermeAnjost2c/mcp-mapeamento-ddp.git
cd mcp-mapeamento-ddp
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure o arquivo `mcp.json` com o caminho correto para o `server.py`

## Uso

### Formato de Entrada

O sistema espera texto estruturado no seguinte formato:

```
# ETAPA 1 - Nome da Etapa
Supplier: Fornecedor da etapa
Input: Entrada da etapa
Process: Processo realizado
Output: Saída da etapa
Customer: Cliente da etapa

# ETAPA 2 - Próxima Etapa
...
```

### Exemplo de Uso

```python
from mcp_mapeamento import criar_ddp

resultado = criar_ddp(
    texto_etapas="texto_estruturado_aqui",
    nome_processo="Processo de Vendas",
    diretorio_saida="./output",
    nome_arquivo="DDP_Vendas.pptx"  # Opcional
)
```

## Configuração

### Template PowerPoint

O sistema utiliza um template PowerPoint (`DDP_TEMPLATE.pptx`) que deve conter os seguintes placeholders:

- **Text Placeholder 1**: Para regras da etapa
- **Text Placeholder 2**: Para nome da etapa
- **Text Placeholder 3**: Para descrição da etapa

### Configurações

As configurações podem ser ajustadas no arquivo `config.py`:

- `TEMPLATE_PATH`: Caminho para o template PowerPoint
- `DEFAULT_CONFIG`: Configurações padrão do sistema
- `PLACEHOLDERS`: Mapeamento de placeholders do template
- `ETAPA_REGEX_PATTERN`: Padrão regex para processamento de etapas

## Dependências

- `fastmcp>=0.1.0`: Framework MCP
- `python-pptx>=0.6.21`: Manipulação de arquivos PowerPoint

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato através dos issues do repositório.
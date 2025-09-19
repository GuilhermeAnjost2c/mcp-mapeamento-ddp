# Instruções para o Template PowerPoint

## Template Necessário

Este projeto requer um template PowerPoint chamado `DDP_TEMPLATE.pptx` que deve ser adicionado ao repositório.

### Como adicionar o template:

1. **Clone o repositório localmente:**
   ```bash
   git clone https://github.com/GuilhermeAnjost2c/mcp-mapeamento-ddp.git
   cd mcp-mapeamento-ddp
   ```

2. **Adicione o arquivo DDP_TEMPLATE.pptx:**
   - Copie o arquivo `DDP_TEMPLATE.pptx` para a raiz do repositório
   - O arquivo deve estar no mesmo diretório que `server.py`

3. **Faça commit e push:**
   ```bash
   git add DDP_TEMPLATE.pptx
   git commit -m "Add PowerPoint template file"
   git push origin main
   ```

### Estrutura do Template

O template PowerPoint deve conter os seguintes placeholders:

- **Text Placeholder 1**: Para regras da etapa (Input, Output, Supplier, Customer)
- **Text Placeholder 2**: Para nome da etapa (ETAPA X - Nome da Etapa)
- **Text Placeholder 3**: Para descrição da etapa

### Layout Recomendado

- Use o layout de slide em branco (índice 5)
- Configure os placeholders conforme especificado acima
- Mantenha o design consistente para todas as etapas

### Verificação

Após adicionar o template, você pode verificar se está funcionando executando:

```python
from config import validate_template_exists
print(validate_template_exists())  # Deve retornar True
```
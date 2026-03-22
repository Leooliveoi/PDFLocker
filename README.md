# OiSecurity PDF Locker - CLI Tool

Uma ferramenta de linha de comando (CLI) minimalista e segura para criptografar arquivos PDF utilizando o padrão **AES-256**. 

### Diferenciais de Segurança
*   **Criptografia AES-256:** Utiliza o algoritmo de criptografia mais robusto disponível na biblioteca `pypdf`.
*   **Input Oculto:** Se a senha não for fornecida via argumento, o script solicita uma entrada protegida (os caracteres não aparecem na tela), evitando que a senha fique registrada no histórico do seu terminal.

---

## Pré-requisitos

Certifique-se de ter o Python 3.x instalado e a biblioteca necessária:

```bash
pip install pypdf
```

---

## Como Usar

O script aceita o caminho do arquivo como argumento obrigatório.

### 1. Forma Recomendada (Senha Oculta)
Execute o script apenas com o caminho do arquivo. O sistema solicitará a senha de forma segura:
```bash
python nome_do_script.py documento.pdf
```

### 2. Forma Direta (Flag de Senha)
Você pode passar a senha diretamente, embora isso possa deixar rastros no histórico do bash/zsh:
```bash
python nome_do_script.py documento.pdf -p "minha_senha_123"
```

---

## Saída
O script não sobrescreve o arquivo original. Ele gera um novo arquivo seguindo o padrão:
`nome_do_arquivo.pdf` ➔ `nome_do_arquivo_protected.pdf`

---

## Notas de Erro
*   **Arquivo não encontrado:** O script valida a existência do PDF antes de iniciar o processo.
*   **Senha Vazia:** O processo é interrompido caso nenhuma senha seja fornecida no prompt interativo.
*   **Interrupção:** Suporta `Ctrl+C` (KeyboardInterrupt) para cancelamento limpo da operação.

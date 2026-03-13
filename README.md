# 🤖 Chatbot com Ollama

Um chatbot inteligente e funcional que utiliza o Ollama com modelos de linguagem local (sem conexão com servidores remotos). O chatbot oferece conversas fluidas, persistência de histórico e diversos comandos úteis.

## 📋 Características

- ✅ **Conversação inteligente** - Usa modelos de IA localmente com Ollama
- ✅ **Sistema de Prompt** - Comportamento personalizável da IA
- ✅ **Histórico Persistente** - Salva todas as conversas em JSON
- ✅ **Timestamps** - Cada mensagem registra quando foi enviada
- ✅ **Comandos Especiais** - Histórico, limpeza, ajuda
- ✅ **Interface Amigável** - Menu intuitivo e mensagens claras
- ✅ **Tratamento de Erros** - Validação e recuperação robusta

## 🔧 Requisitos

- Python 3.8+
- Ollama instalado e rodando
- Biblioteca `ollama` para Python

## 📦 Instalação

### 1. Instale o Ollama

Baixe em: [https://ollama.ai](https://ollama.ai)

### 2. Instale a dependência Python

```bash
pip install ollama
```

### 3. Puxe um modelo (primeira execução)

```bash
ollama pull llama3.2:3b
```

Ou use outro modelo disponível:
- `llama2` - Modelo Llama 2
- `llama3.2:1b` - Llama 3.2 com 1 bilhão de parâmetros (muito rápido)
- `neural-chat` - Modelo otimizado para chat

## 🚀 Como Usar

### Inicie o Ollama

Abra uma janela de terminal e execute:

```powershell
ollama serve
```

Deixe rodando em background.

### Execute o Chatbot

```powershell
python chatbot.py
```

### Interaja com o Chatbot

```
============================================================
🤖 CHATBOT COM OLLAMA
============================================================
Comandos especiais:
  • 'histórico' - Ver histórico de mensagens
  • 'limpar' - Limpar histórico
  • 'ajuda' - Mostrar ajuda
  • 'sair' - Encerrar conversa
============================================================

Você: Olá! Como você está?

Chatbot: Olá! Estou funcionando bem, obrigado por perguntar. 
Como posso ajudá-lo hoje?
```

## 📖 Comandos Disponíveis

| Comando | Descrição |
|---------|-----------|
| `histórico` | Mostra todas as mensagens com timestamps |
| `limpar` | Limpa o histórico de conversa |
| `ajuda` | Exibe menu de ajuda |
| `sair` | Encerra o programa (Ctrl+C também funciona) |

## 📁 Estrutura do Código

### Classe `Chatbot`

A classe principal que gerencia toda a funcionalidade:

```python
class Chatbot:
    def __init__(self, modelo, system_prompt)
    def carregar_historico()        # Carrega conversas anteriores
    def salvar_historico()          # Salva em JSON
    def ler_mensagem_usuario()      # Lê entrada com validação
    def enviar_mensagem()           # Envia para Ollama e obtém resposta
    def exibir_historico()          # Mostra todas as mensagens
    def limpar_historico()          # Remove histórico
    def iniciar()                   # Loop principal do chatbot
```

### Componentes-chave

**1. System Prompt**
```python
SYSTEM_PROMPT = """Você é um assistente de IA inteligente, amigável e útil. 
Você ajuda o usuário com dúvidas, tarefas e conversas.
Sempre seja respeitoso, claro e conciso.
Se não sabe a resposta, diga que não sabe."""
```
Define como a IA deve se comportar.

**2. Configuração**
```python
MODELO = "llama3.2:3b"              # Modelo usado
ARQUIVO_HISTORICO = "historico_conversa.json"  # Arquivo de persistência
```

**3. Histórico de Mensagens**
Cada mensagem é armazenada como:
```json
{
  "role": "user",           // ou "assistant"
  "content": "mensagem",
  "timestamp": "2026-03-13T10:30:00.123456"
}
```

## 🔄 Fluxo de Funcionamento

1. **Inicialização** → Carrega histórico anterior
2. **Entrada** → Aguarda mensagem do usuário
3. **Processamento** → Valida e processa entrada
4. **Envio** → Envia para Ollama com contexto do histórico
5. **Resposta** → Exibe resposta e salva no histórico
6. **Loop** → Volta ao passo 2

## 💾 Arquivo de Histórico

O arquivo `historico_conversa.json` é criado automaticamente:

```json
[
  {
    "role": "user",
    "content": "Olá!",
    "timestamp": "2026-03-13T10:30:00.123456"
  },
  {
    "role": "assistant",
    "content": "Olá! Como posso ajudá-lo?",
    "timestamp": "2026-03-13T10:30:05.654321"
  }
]
```

## ⚙️ Personalização

### Mudar o Modelo

Edite a variável `MODELO` no arquivo:

```python
MODELO = "llama2"  # ou outro modelo
```

### Customizar o Comportamento

Altere o `SYSTEM_PROMPT`:

```python
SYSTEM_PROMPT = """Você é um especialista em programação Python.
Sempre forneça exemplos de código quando relevante."""
```

## 🐛 Solução de Problemas

**Erro: "Erro ao conectar com Ollama"**
- Certifique-se de que o Ollama está rodando: `ollama serve`
- Verifique se o modelo foi baixado: `ollama list`

**Erro: "FileNotFoundError" ao salvar**
- Verifique permissões de escrita no diretório

**Modelo muito lento**
- Use um modelo menor como `llama3.2:1b`

## 📊 Exemplo de Conversa Completa

```
============================================================
🤖 CHATBOT COM OLLAMA
============================================================

Você: Qual é a capital da França?

Chatbot: A capital da França é Paris. É uma das cidades mais 
famosas do mundo, conhecida pela Torre Eiffel, museus como o Louvre,
e sua contribuição significativa para arte, cultura e história.

Você: histórico

============================================================
HISTÓRICO DE CONVERSA
============================================================

[2026-03-13T10:30:00.123456] Você:
Qual é a capital da França?

[2026-03-13T10:30:05.654321] Chatbot:
A capital da França é Paris...

============================================================

Você: sair

============================================================
Até logo! Histórico salvo em 'historico_conversa.json'
============================================================
```

## 📝 Notas Importantes

- O histórico é mantido em memória durante a sessão e salvo em JSON
- Fechar o programa sem usar "sair" ainda salva o histórico automaticamente
- O Ollama deve estar em execução para o chatbot funcionar
- Modelos maiores precisam de mais RAM e são mais lentos
- A primeira resposta pode demorar mais enquanto o modelo carrega

## 🤝 Contribuições

Sinta-se livre para modificar e melhorar o código conforme suas necessidades!

## 📄 Licença

Este projeto é fornecido como está, sem garantias.

---

**Desenvolvido com ❤️ usando Python e Ollama**

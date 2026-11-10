# Chatbot com LLM local (Ollama)

Chatbot de terminal em Python que conversa com um modelo de linguagem rodando na própria máquina, via [Ollama](https://ollama.com). Nenhuma mensagem sai do computador.

Fiz este projeto para entender na prática como funciona a conversa com um LLM: como o prompt de sistema define o comportamento do modelo, como o histórico é reenviado a cada mensagem para manter o contexto e como guardar essa conversa entre execuções.

## O que ele faz

- Usa o **Llama 3.2 (3B)** por padrão; o modelo é configurável.
- **Prompt de sistema** editável, para mudar o comportamento do assistente.
- **Histórico persistente** em JSON, com data e hora de cada mensagem. A conversa continua de onde parou quando o programa é aberto de novo.
- **Contexto completo:** a cada mensagem, o histórico inteiro é enviado ao modelo junto com o prompt de sistema.
- Comandos `histórico`, `limpar`, `ajuda` e `sair`.
- Tratamento de erros quando o Ollama não está rodando e validação de entrada vazia.

## Como funciona

```
entrada do usuário
      │
      ▼
histórico (JSON) + prompt de sistema ──► ollama.chat(modelo) ──► resposta
      ▲                                                            │
      └──────────────── salva mensagem e resposta ◄────────────────┘
```

Toda a lógica fica na classe `Chatbot` (`chatbot.py`): carregar e salvar o histórico, ler a entrada, enviar ao modelo e tratar os comandos.

## Como rodar

Requisitos: Python 3.8+ e o Ollama instalado.

```bash
pip install ollama
ollama pull llama3.2:3b
ollama serve          # em outro terminal
python chatbot.py
```

Para trocar o modelo ou o comportamento, edite `MODELO` e `SYSTEM_PROMPT` no início de `chatbot.py`. Modelos menores, como `llama3.2:1b`, respondem mais rápido em máquinas com pouca memória.

## Próximos passos

Este chatbot foi a base do meu assistente com RAG sobre as diretrizes da UFPA (link a adicionar quando publicar), que acrescenta recuperação de documentos para responder com base em textos oficiais.

---
Adryele Oliveira · [GitHub](https://github.com/elleoliveir) · [Lattes](http://lattes.cnpq.br/1980321616960828)

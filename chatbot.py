import ollama
import json
from datetime import datetime


# System prompt define o comportamento do chatbot
SYSTEM_PROMPT = """Você é um assistente de IA inteligente, amigável e útil. 
Você ajuda o usuário com dúvidas, tarefas e conversas.
Sempre seja respeitoso, claro e conciso.
Se não sabe a resposta, diga que não sabe."""

# Configuração
MODELO = "llama3.2:3b"
ARQUIVO_HISTORICO = "historico_conversa.json"


class Chatbot:
    """Classe que gerencia o chatbot com histórico de mensagens."""
    
    def __init__(self, modelo=MODELO, system_prompt=SYSTEM_PROMPT):
        """Inicializa o chatbot."""
        self.modelo = modelo
        self.system_prompt = system_prompt
        self.historico = []  # Lista de mensagens
        self.carregar_historico()
    
    def carregar_historico(self):
        """Carrega histórico de conversas anteriores."""
        try:
            with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as arquivo:
                self.historico = json.load(arquivo)
                print(f"✓ Histórico carregado: {len(self.historico)} mensagens\n")
        except FileNotFoundError:
            print("ℹ Iniciando novo histórico de conversa\n")
            self.historico = []
    
    def salvar_historico(self):
        """Salva o histórico de mensagens em arquivo JSON."""
        try:
            with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as arquivo:
                json.dump(self.historico, arquivo, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Erro ao salvar histórico: {e}")
    
    def ler_mensagem_usuario(self):
        """Lê a mensagem do usuário com validação."""
        while True:
            try:
                mensagem = input("\nVocê: ").strip()
                
                if not mensagem:
                    print("⚠ Por favor, digite algo.")
                    continue
                
                if mensagem.lower() in ["sair", "quit", "exit"]:
                    return None
                
                return mensagem
            
            except KeyboardInterrupt:
                return None
    
    def enviar_mensagem(self, mensagem):
        """Envia mensagem para Ollama e obtém resposta."""
        try:
            # Adiciona a mensagem do usuário ao histórico
            self.historico.append({
                "role": "user",
                "content": mensagem,
                "timestamp": datetime.now().isoformat()
            })
            
            # Prepara as mensagens para o modelo
            mensagens_modelo = [msg for msg in self.historico if msg["role"] in ["user", "assistant"]]
            
            # Envia para Ollama
            resposta = ollama.chat(
                model=self.modelo,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    *mensagens_modelo
                ]
            )
            
            # Extrai o conteúdo da resposta
            conteudo_resposta = resposta["message"]["content"]
            
            # Adiciona a resposta ao histórico
            self.historico.append({
                "role": "assistant",
                "content": conteudo_resposta,
                "timestamp": datetime.now().isoformat()
            })
            
            # Salva o histórico
            self.salvar_historico()
            
            return conteudo_resposta
        
        except Exception as e:
            print(f"✗ Erro ao conectar com Ollama: {e}")
            print("ℹ Certifique-se de que o Ollama está rodando.\n")
            return None
    
    def exibir_historico(self):
        """Exibe o histórico completo da conversa."""
        if not self.historico:
            print("\n📋 Histórico vazio.")
            return
        
        print("\n" + "=" * 60)
        print("HISTÓRICO DE CONVERSA")
        print("=" * 60)
        
        for msg in self.historico:
            timestamp = msg.get("timestamp", "N/A")
            role = "Você" if msg["role"] == "user" else "Chatbot"
            content = msg["content"]
            print(f"\n[{timestamp}] {role}:")
            print(f"{content}")
        
        print("\n" + "=" * 60 + "\n")
    
    def limpar_historico(self):
        """Limpa o histórico de conversas."""
        confirmacao = input("Tem certeza que deseja limpar o histórico? (s/n): ").lower()
        if confirmacao == "s":
            self.historico = []
            self.salvar_historico()
            print("✓ Histórico limpo.\n")
        else:
            print("Cancelado.\n")
    
    def iniciar(self):
        """Inicia o loop principal do chatbot."""
        self._exibir_menu_inicial()
        
        while True:
            mensagem = self.ler_mensagem_usuario()
            
            if mensagem is None:
                self._exibir_menu_despedida()
                break
            
            # Verificar comandos especiais
            if mensagem.lower() == "histórico":
                self.exibir_historico()
                continue
            elif mensagem.lower() == "limpar":
                self.limpar_historico()
                continue
            elif mensagem.lower() == "ajuda":
                self._exibir_ajuda()
                continue
            
            # Enviar mensagem normal
            resposta = self.enviar_mensagem(mensagem)
            if resposta:
                print(f"\nChatbot: {resposta}")
    
    def _exibir_menu_inicial(self):
        """Exibe menu inicial."""
        print("\n" + "=" * 60)
        print("🤖 CHATBOT COM OLLAMA")
        print("=" * 60)
        print("Comandos especiais:")
        print("  • 'histórico' - Ver histórico de mensagens")
        print("  • 'limpar' - Limpar histórico")
        print("  • 'ajuda' - Mostrar ajuda")
        print("  • 'sair' - Encerrar conversa")
        print("=" * 60 + "\n")
    
    def _exibir_menu_despedida(self):
        """Exibe mensagem de despedida."""
        print("\n" + "=" * 60)
        print("Até logo! Histórico salvo em 'historico_conversa.json'")
        print("=" * 60 + "\n")
    
    def _exibir_ajuda(self):
        """Exibe menu de ajuda."""
        print("\n" + "=" * 60)
        print("AJUDA")
        print("=" * 60)
        print("Este é um chatbot que funciona localmente com Ollama.")
        print("Você pode conversar normalmente ou usar comandos especiais.")
        print("\nComandos disponíveis:")
        print("  • histórico - Vê todas as mensagens da conversa")
        print("  • limpar - Remove o histórico de conversa")
        print("  • ajuda - Mostra esta mensagem")
        print("  • sair - Encerra o programa")
        print("=" * 60 + "\n")


def main():
    """Função principal."""
    try:
        chatbot = Chatbot(modelo=MODELO, system_prompt=SYSTEM_PROMPT)
        chatbot.iniciar()
    except Exception as e:
        print(f"Erro fatal: {e}")


if __name__ == "__main__":
    main()

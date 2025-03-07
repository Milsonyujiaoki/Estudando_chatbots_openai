import os
from dotenv import load_dotenv
import openai
import asyncio
from openai import APIConnectionError, RateLimitError, APIError, NotFoundError

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path=r"C:\Projetos\Pessoal\Microsoft\TESTES\.env")  # Corrigido o caminho

# Define sua chave de API da OpenAI a partir da variável de ambiente
openai.api_key = os.getenv('OPENAI_API_KEY')

# Inicializa o cliente assíncrono
client = openai.AsyncOpenAI(
    api_key=openai.api_key,
    max_retries=4,
    timeout=20.0
)

# Função assíncrona para interagir com o Assistente
async def interagir_com_assistente(mensagem_usuario):
    try:
        # Recupera o assistente
        assistant = await client.beta.assistants.retrieve("asst_rhFLyYpv6nFMHnX7mmUzb2xv")
        print(f"Assistente recuperado: {assistant.name}")

        # Verifica se a Thread existe
        try:
            thread = await client.beta.threads.retrieve("thread_G8ttyitsHYSb5h2nEXgWEOV6")
            print(f"Thread recuperada: {thread.id}")
        except NotFoundError:
            print("Thread não encontrada. Criando uma nova...")
            thread = await client.beta.threads.create()
            print(f"Nova thread criada: {thread.id}")

        # Adiciona uma mensagem à thread
        message = await client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=mensagem_usuario
        )
        print("Mensagem adicionada à thread com sucesso.")

        # Executa o Assistente
        run = await client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistant.id,
            instructions="Responda ao usuário com base na conversa anterior e com base no pdf fornecido."
        )

        # Verifica status da execução
        if run.status == "completed":
            messages = await client.beta.threads.messages.list(thread_id=thread.id)
            
            for msg in messages.data:  # Exibir na ordem correta
                if msg.role == "assistant":
                    return msg.content[0].text.value
            else:
                return "Nenhuma mensagem encontrada na thread."
        elif run.status == "failed":
            print("❌ A execução do assistente falhou. Capturando detalhes...")
            error_message = getattr(run, 'error', None)
            return f"Motivo: {error_message}" if error_message else "Motivo desconhecido. Verifique os logs da API."
        else:
            return f"Status da execução: {run.status}"

    except APIConnectionError as e:
        return f"O servidor não pôde ser alcançado: {e}"
    except RateLimitError:
        return "Erro 429: Limite de requisições excedido. Aguarde um momento antes de tentar novamente."
    except APIError as e:
        return f"Erro na API com status {e.http_status}: {e}"
    except NotFoundError:
        return "Erro: O assistente ou a thread não foram encontrados. Verifique os IDs e tente novamente."

# Função principal para gerenciar a interação
async def main():
    while True:
        mensagem = input("Você: ")
        if mensagem.lower() in ['sair', 'exit', 'quit']:
            print("Encerrando a conversa. Até logo!")
            break

        resposta = await interagir_com_assistente(mensagem)  # Captura a última resposta
        print(f"Resposta armazenada: {resposta}")  # Armazena e exibe para uso posterior

# Executa o loop assíncrono
asyncio.run(main())

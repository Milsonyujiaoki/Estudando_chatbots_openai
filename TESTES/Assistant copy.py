import os
from dotenv import load_dotenv
import openai
import asyncio
from openai import APIConnectionError, RateLimitError, APIError, NotFoundError

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path="C:\Projetos\Pessoal\Microsoft\TESTES\.env")

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
        # Lista os assistentes disponíveis no projeto atual
        assistants = await client.beta.assistants.list()
        if not assistants.data:
            print("Nenhum assistente encontrado! Verifique se você criou um assistente no projeto correto.")
            return

        # Seleciona o primeiro assistente disponível
        assistant = assistants.data[0]  
        print(f"Usando assistente: {assistant.name} (ID: {assistant.id})")

        # Verifica se a Thread existe
        try:
            thread = await client.beta.threads.retrieve("thread_thddDtGOVSkmntnj3iDGKhh3")
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
            instructions="Responda ao usuário com base na conversa anterior."
        )

        # Exibe a resposta
        if run.status == "completed":
            messages = await client.beta.threads.messages.list(thread_id=thread.id)
            for msg in messages.data[::-1]:  # Exibir na ordem correta
                print(f"ChatGPT: {msg.content[0].text.value}")
        else:
            print(f"Execução em andamento. Status: {run.status}")

    except APIConnectionError as e:
        print("O servidor não pôde ser alcançado")
        print(e)
    except RateLimitError:
        print("Erro 429: Limite de requisições excedido. Aguarde um momento antes de tentar novamente.")
    except APIError as e:
        print(f"Erro na API com status {e.http_status}")
        print(e)
    except NotFoundError:
        print("Erro: O assistente ou a thread não foram encontrados. Verifique os IDs e tente novamente.")

# Função principal para gerenciar a interação
async def main():
    while True:
        mensagem = input("Você: ")
        if mensagem.lower() in ['sair', 'exit', 'quit']:
            print("Encerrando a conversa. Até logo!")
            break

        await interagir_com_assistente(mensagem)

# Executa o loop assíncrono
asyncio.run(main())
import os
from dotenv import load_dotenv
import telegram
from telegram.ext import Application, CommandHandler, MessageHandler
import google.generativeai as genai

# Carrega as variáveis do arquivo .env
load_dotenv()

# Acesse as variáveis
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

genai.configure(api_key=GOOGLE_API_KEY)

# Crie uma aplicação de bot
application = (
    Application.builder().token(TELEGRAM_BOT_TOKEN).build()
)

# Instrução do sistema e histórico do chat
system_instruction = "Voce é um Veterinario, que vai avaliar resultados de exames de sangue, quero que voce avalie o resultado de acordo com os valores de referencia, os que estiverem dentro dos \
      valores de referencia nao faz nada, mas os que estão fora dos valores de referencia, quero que faça uma explicação e uma justificativa da causa e recomende alguma solução para melhora, podendo ser \
         remedio ou exercicios ou outra coisa com poucas palavras"
chat_history = []

# Cria o modelo generativo
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest", system_instruction=system_instruction)
chat = model.start_chat(history=chat_history)

async def start(update, context):
    global chat_history

    # Gera a apresentação do padeiro João
    response = chat.send_message("Se apresente como o Dr. VetBot e diga que voce pode avaliar os resultados de exames do pet e peça para enviar o exame, os valores de referencias e o resultado em poucas palavras")
    chat_history.append({"role": "bot", "content": response.text})

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=response.text
    )

async def respond(update, context):
    global chat_history

    if update.message.text:
        user_message = update.message.text
        
        # Adiciona a mensagem do usuário ao histórico
        chat_history.append({"role": "user", "content": user_message})
        
        # Gera a resposta usando o histórico
        response = chat.send_message(user_message)
        
        # Adiciona a resposta do bot ao histórico
        chat_history.append({"role": "bot", "content": response.text})

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=response.text
        )

# Adiciona handlers para os comandos
application.add_handler(CommandHandler('start', start))
application.add_handler(
    MessageHandler(
        telegram.ext.filters.TEXT & ~telegram.ext.filters.COMMAND,
        respond
    )
)

# Inicia o bot
application.run_polling()
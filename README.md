## Bot do Telegram com o Gemini

Este projeto demonstra um bot do Telegram que utiliza a API do Google Generative AI (Gemini) para fornecer informações sobre exames de sangue de animais de estimação.

### Funcionamento

O bot funciona da seguinte maneira:

1. **Inicialização:**
   - O bot é iniciado ao enviar qualquer mensagem.
   - Ele se apresenta como o Dr. VetBot e solicita que o usuário envie o resultado do exame, os valores de referência e uma breve descrição da situação.

2. **Análise de Exames:**
   - O bot recebe a mensagem do usuário com os dados do exame e a envia para a API do Gemini.
   - A API do Gemini processa a informação e gera uma resposta baseada no modelo definido, que inclui uma análise dos resultados do exame, uma explicação dos valores fora da faixa normal e uma recomendação para o dono do animal.

3. **Resposta do Bot:**
   - O bot envia a resposta gerada pelo Gemini para o usuário, fornecendo informações claras e concisas sobre a análise dos exames.

### Pré-requisitos

* Conta do Google Cloud com acesso à API do Google Generative AI.
* Conta do Telegram para criar um bot.
* Python 3.7 ou superior instalado.
* Bibliotecas necessárias instaladas: `python-telegram-bot`, `google-generativeai`, `python-dotenv`.

### Como usar

1. **Crie uma conta no Google Cloud e ative a API do Generative AI:** [https://console.cloud.google.com/](https://console.cloud.google.com/)
2. **Crie um bot no Telegram:** [https://core.telegram.org/bots](https://core.telegram.org/bots)
3. **Crie um arquivo `.env` na raiz do projeto:**
com o GOOGLE_API_KEY=sua_chave_de_api_aqui e o TELEGRAM_BOT_TOKEN=seu_token_do_bot_aqui
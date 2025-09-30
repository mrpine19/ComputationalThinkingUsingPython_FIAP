import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Pega a chave da API das variáveis de ambiente e a configura
# A biblioteca do Google também pode fazer isso automaticamente se o nome da variável for GOOGLE_API_KEY
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Cria o modelo
model = genai.GenerativeModel('gemini-2.5-flash')

# Gera o conteúdo
try:
    response = model.generate_content("Quando falamos de LLM, o que seria um token? Como saber quantos tokens essa requisição, por exemplo, custa?")
    print(response.text)
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    print("\nVerifique se a sua API Key está correta no arquivo .env e se o nome da variável é 'GOOGLE_API_KEY'.")
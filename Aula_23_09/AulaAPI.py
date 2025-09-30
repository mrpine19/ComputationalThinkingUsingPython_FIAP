# Partes de uma URL (Uniform Resource Locator):
#
# Esquema, Domínio, Porta, Caminho e Query String


# 1. Esquema (Scheme): Indica o protocolo de comunicação.

# Os esquemas mais comuns em sistemas web são o "http" e o "https".

# O HTTP (Hypertext Transfer Protocol) é utilizado para transferir
# informações entre um cliente e um servidor.

# Ele permite que os clientes solicitem recursos
# (páginas da web, imagens, JSON, dados, etc)
# e os servidores respondam fornecendo esses recursos.

# Opera no modelo de solicitação-resposta (request-response),
# onde o **cliente faz requests** para URLs e o
# **servidor responde (responses)** com os dados solicitados.

# As mensagens HTTP incluem métodos, como GET para buscar recursos
# e POST para enviar dados,
# além de códigos de status.
# 200 == OK
# 404 == Not Found (não encontrado)

# O HTTPS é a versão "segura" do HTTP, pois utiliza
# criptografia para que as informações sejam acessíveis
# apenas para o cliente e o servidor.


# 2. **Domínio (Host)**: Indica o endereço do servidor onde o
# recurso está localizado.
# Pode ser um domínio como https://www.google.com ou um endereço
# de IP https://142.250.219.4:443 (Google)
# DNS recebe um domínio traduz para (endereço) IP

# 3. **Porta (Port)**: é opcional e indica o número da porta de
# um servidor a ser usado para acessá-lo.
# Se não for especificada, utiliza-se a porta padrão para o esquema
# como por exemplo, 80 para HTTP e 443 para HTTPS.

# No exemplo anterior: https://www.google.com:443 ou
# https://142.250.219.4:443


# 4. **Caminho (Path)**: (opcional)
# Especifica o caminho para o recurso no servidor.
# Pode incluir diretários e subdiretários.
# Exemplos:
# https://www.google.com/search  => Google search
# https://www.google.com/imghp  => Google imagens


# 5. **Query String**: (opcional)
# Contém os parâmetros de consulta para o servidor.
# É precedida por um ponto de interrogação "?" e
# pode conter múltiplos pares chave-valor separados por "&".

# Exemplo: https://www.google.com/search?q=fiap

'''
A API (Application Programming Interface) é uma interface para disponibilizar
seu serviço/recurso para 'qualquer' pessoa, lugar ou forma de uso.
Ao construirmos APIs, nós disponibilizamos uma URL para receber requisições (requests)
e devolver respostas (responses)

'''


# Acessando uma API com Python
# para interagir com uma API (enviar requests), temos a biblioteca requests:
# caso ainda não tenham instalado, no terminal, digitem:
# pip install requests
import requests
#sintaxe: requests.METODO(url)  <- a URL deve ser uma string
CEP_DESEJADO = '99999999'
resposta = requests.get(f'https://viacep.com.br/ws/{CEP_DESEJADO}/json/')
# a resposta é um objeto com vários atributos. Os principais, são:
# - resposta.status_code: um número com o status da resposta da requisição
#     LEMBRANDO QUE só teremos resposta caso a requisição tenha um status 'ok'
# - resposta.json(): retorna em formato de json SE APLICÁVEL a resposta obtida
if resposta.status_code == 200: #se der certo e eu receber resposta...
    #apenas se tiver resposta, eu consigo converter em json e printar
    resposta_json = resposta.json()
    if resposta_json == {'erro': 'true'}:
        print ("CEP Não localizado!")
    else:
        print(resposta.status_code)
        print(type(resposta.json()))
else:
    print("ERRO! Formato do CEP inválido. Código Número: ", resposta.status_code)
    print("Consulte a documentação em https://viacep.com.br/ para saber mais ")

#EXERCÍCIO:
#coloque este script numa função que receba um cep como parâmetro, e que
# contenha um validador prévio de formato do CEP,
# de forma com a qual não recebamos status 400


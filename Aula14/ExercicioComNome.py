#Digitar nome e sobrenome. Cada nome deve ter ao menos 2 caracteres. No final, dizer quantos erros teve
tentativas = 0

while True:

    nome = input("Digite seu nome completo: ")
    nome_split = nome.split(" ")

    nome_escrito_corretamente = True

    tamanho_nome = len(nome_split)
    for i in range(tamanho_nome):
        tamanho_nome_verificado = len(nome_split[i])

        if(tamanho_nome_verificado < 2):
            print("Nome invalido. Tente novamente.")
            tentativas += 1
            nome_escrito_corretamente = False
            break

    if (nome_escrito_corretamente):
        print(f"Número de tentativas: {tentativas}")
        break
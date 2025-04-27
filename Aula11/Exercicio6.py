# 6) faça um programa que solicite ao usuário um número N obrigatoriamente inteiro entre 1 e 20
# este número N vai ser a quantidade de novos números a serem digitados pelo usuário
# ao terminar de digitar estes N números, o programa deverá imprimir:
# ## o maior valor
# ## o menor valor
# ## a soma de todos os valores
# ## a média de todos os valores
# ## quantos porcento dos valores foram positivos
# ## quantos porcento dos valores foram negativos

# Solicita um número inteiro entre 1 e 20
qtd_de_numeros = int(input("Digite um número entre 1 e 20: "))

while qtd_de_numeros < 1 or qtd_de_numeros > 20:
    qtd_de_numeros = int(input("Número inválido. Digite um número entre 1 e 20: "))

#Obtem o primeiro número para inicializar as variáveis maior_valor, menor_valor e soma
primeiro_numero = float(input("Digite o 1º número: "))
maior_valor = primeiro_numero
menor_valor = primeiro_numero
soma = primeiro_numero

#Inicializando as variáveis qtd_valores_positivos e qtd_valores_negativos de acordo com o primeiro número digitado
if primeiro_numero > 0:
    qtd_valores_positivos = 1
    qtd_valores_negativos = 0
else:
    qtd_valores_positivos = 0
    qtd_valores_negativos = 1

for i in range(2, qtd_de_numeros + 1):
    numero_atual = float(input(f"Digite o {i}º número: "))

    # Atualiza maior e menor valor
    if numero_atual > maior_valor:
        maior_valor = numero_atual
    if numero_atual < menor_valor:
        menor_valor = numero_atual

    soma += numero_atual

    # Conta positivos e negativos
    if numero_atual > 0:
        qtd_valores_positivos += 1
    else:
        qtd_valores_negativos += 1

# Cálculos finais
media = soma / qtd_de_numeros
porcentagem_positivos = qtd_valores_positivos * 100 / qtd_de_numeros
porcentagem_negativos = qtd_valores_negativos * 100 / qtd_de_numeros

# Exibir resultados

print(f"O maior número é {maior_valor:.2f} e o menor número é {menor_valor:.2f}. \nA soma total é {soma:.2f}, assim como a média foi {media:.2f}.")
print(f"Para finalizar, a porcentagem de números positivos e negativos foram {porcentagem_positivos:.2f}% e {porcentagem_negativos:.2f}%, respectivamente.")
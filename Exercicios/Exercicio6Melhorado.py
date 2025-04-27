# 6) faça um programa que solicite ao usuário um número N obrigatoriamente inteiro entre 1 e 20
# este número N vai ser a quantidade de novos números a serem digitados pelo usuário
# ao terminar de digitar estes N números, o programa deverá imprimir:
# ## o maior valor
# ## o menor valor
# ## a soma de todos os valores
# ## a média de todos os valores
# ## quantos porcento dos valores foram positivos
# ## quantos porcento dos valores foram negativos

def processar_numeros(qtd_de_numeros):
    """Solicita N números do usuário e imprime estatísticas sobre eles."""
    maior_valor = float('-inf') #Representa infinito negativo (-∞), menor que qualquer número real.
    menor_valor = float('inf') #Representa infinito positivo (+∞), maior que qualquer número real.
    soma = 0
    qtd_valores_positivos = 0
    qtd_valores_negativos = 0

    for i in range(1, qtd_de_numeros + 1):
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
    print(f"\nO maior número é {maior_valor:.2f} e o menor número é {menor_valor:.2f}.")
    print(f"A soma total é {soma:.2f}, e a média dos valores foi {media:.2f}.")
    print(f"Percentual de números positivos: {porcentagem_positivos:.2f}%")
    print(f"Percentual de números negativos: {porcentagem_negativos:.2f}%")

# Solicita um número inteiro entre 1 e 20
qtd_de_numeros = int(input("Digite um número entre 1 e 20: "))

while qtd_de_numeros < 1 or qtd_de_numeros > 20:
    qtd_de_numeros = int(input("Número inválido. Digite um número entre 1 e 20: "))

# Executa a função
processar_numeros(qtd_de_numeros)
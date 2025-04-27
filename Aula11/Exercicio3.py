# 3) faça um programa que imprima a soma dos números inteiros positivos de 1 a 100, inclusive
# faça este exercício uma vez utilizando o for, e outra utilizando o while

#SOLUÇÃO USANDO FOR
soma_for = 0
for numero in range(1, 101):
    soma_for = soma_for + numero

print(f"O resultado da soma usando for é {soma_for}")

#SOLUÇÃO USANDO WHILE
contador = 1
soma_while = 0
while contador <= 100:
    soma_while += contador
    contador += 1

print(f"O resultado da soma usando while é {soma_while}")
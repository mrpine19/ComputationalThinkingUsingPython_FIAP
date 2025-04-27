# 4) imprima a tabuada do número 5, entre 0 e 10, inclusive, tanto utiliando o for quanto o while
# Depois, adapte o programa para receber dois números do usuário: o de início e o de fim
# faça este exercício uma vez utilizando o for, e outra utilizando o while

#TABUADA DO 5 USANDO FOR
print("Início da tabuada usando for")

for i in range(0, 11):
    print(f"5 * {i} = {i * 5}")

print("Fim da tabuada usando for")
print()
print("----------------------------------------------")
print()
#TABUADA DO 5 USANDO WHILE
print("Inicio da tabuada usando while")
contador = 0
while contador <= 10:
    print(f"5 * {contador} = {contador * 5}")
    contador += 1
print("Fim da tabuada usando while")
print()
print("----------------------------------------------")
print()
print("Inicio da tabuada recebendo inicio e fim do usuário")
inicio = int(input("Digite o número inicio da tabuada: "))
fim = int(input("Digite o número fim da tabuada: "))

while inicio > fim:
    fim = int(input("Número de ínicio maior que o número de fim. Digite novamente: "))
print()
print("----------------------------------------------")
print()
print("Inicio da tabuada usando for")
for i in range(inicio, fim + 1):
    print(f"5 * {i} = {i * 5}")
print("Fim da tabuada usando for")
print()
print("----------------------------------------------")
print()
print("Inicio da tabuada usando while")
contador = inicio
while contador <= fim:
    print(f"5 * {contador} = {contador * 5}")
    contador += 1
print("Fim da tabuada usando while")
print("Fim da tabuada recebendo inicio e fim do usuário")
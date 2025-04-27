# 2) Solicitar um número obrigatoriamente inteiro positivo do usuário, e calcular seu fatorial

print("-------------CALCULANDO FATORIAL-----------------")
num = int(input("Digite um número inteiro e positivo: "))

while num < 0:
    num = int(input("O número digitado é negativo! Digite novamente: "))

fatorial = 1
for i in range(num, 1, -1):
    fatorial = fatorial * i

print(f"O fatorial de {num} é igual a {fatorial}")
print("-------------FIM-----------------")
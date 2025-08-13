'''
1, 1, 2, 3, 5, 8, 13, 21
'''


numero = int(input("Digite o número: "))

sequencia = [1, 1]
print(sequencia)

while sequencia[-1] < numero:
    proximo_numero = sequencia[-1] + sequencia[-2]
    sequencia.append(proximo_numero)
    print(sequencia)

print("O próximo número maior que ",numero," da sequencia de Fibonacci é ", sequencia[-1])




print("---------------------------------")
'''
item_da_sequencia = 30
primeiro_numero = 1
segundo_numero = 1

for i in range(2, item_da_sequencia):
    proximo_numero_sequencia = primeiro_numero + segundo_numero
    primeiro_numero = segundo_numero
    segundo_numero = proximo_numero_sequencia

print(f"{item_da_sequencia}º termo da sequência: {segundo_numero}")
'''

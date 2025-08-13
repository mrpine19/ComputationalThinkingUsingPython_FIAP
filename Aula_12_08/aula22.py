#Vamos programar a sequencia de Fibonacci
#Obs: a sequencia de fibonacci é formada somando os 2 últimos números da sequencia para
#obter o próximo:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987

'''
Ideia: chegar em uma fórmula que possa ser repetida em um loop
-> PENSAMENTO INICIAL:
l = [1,1]
f = l[-1]+l[-2]
l.append(f)
'''

'''
-- Primeiro pensamento: fizemos uma lista que cresce para calcular todos os números
-- Segundo pensamento: percebemos que a lista não precisa crescer, por só me importa
os 2 últimos números

item_da_sequencia = 10
l = [1, 1]
for i in range(2, item_da_sequencia):
    f = l[-1] + l[-2]
    l.append(f)
    l.pop(0) #entrego o índice apenas com o número
    # é importante aqui o pop ser depois do cálculo
print(l[1])
print(l)

-- Terceiro pensamento: como a quantidade de números que trabalhamos é fixa (entre 2 e 3),
podemos trabalhar apenas com variáveis de memória (sem precisar usar lista)
'''
item_da_sequencia = 10
primeiro_numero = 1
segundo_numero = 1
#aqui eu preciso necessariamente de 3 valores,
#pois ao alterar um valor no python, eu não tenho como recuperar o que era antes
#então, eu preciso de um intermediário para guardar o novo número da sequencia
#antes de fazer as substituições
for i in range(2, item_da_sequencia):
    proximo_numero_sequencia = primeiro_numero + segundo_numero #é o equivalente a f = l[-1] + l[-2], porém sem usar lista
    primeiro_numero = segundo_numero
    segundo_numero = proximo_numero_sequencia
print(f"{item_da_sequencia}º termo da sequência: {segundo_numero}")

# E se eu quiser transformar isto em uma função?
# Ex1: criar uma função que retorne o n-ésimo item da sequencia
# Ex2: criar uma função que retorne o fatorial de um número
#   (o fatorial de n é a multiplicação de todos os números entre 1 e n -inclusive)
#   4! = 4*3*2*1
# Ex3: transformar as funções acima em funções recursivas (que chamam elas mesmas)
    #aqui, vocês tem que pensar em uma outra forma de parar
    #( +- a filosofica do while True: tem que ter um critério de parada para não ser infinito)
    
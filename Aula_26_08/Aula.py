### REVISÃO CP4
'''
- *args na função -> forma de receber qualquer quantidade
- quando temos funções com vários parâmetros e args, podemos indicar por nome o que queremos definir
- há 3 principais formas de importar bibliotecas:
    - import math          -> aqui eu importo toda a biblioteca. Para usar, tem que colocar math.função
    - from math import *   -> aqui eu importo toda a biblioteca. Para usar, basta chamar a função diretamente
        (cuidado! caso tenha uma função com mesmo nome que alguma no seu programa, vai sobrescrever)
    - from math import sin as seno  -> aqui eu estou importando apenas a função 'sin' e renomeando como 'seno'

- tuplas são "listas que não mudam" (nem o tamanho nem os itens)
    - o que caracteriza a tupla é a vírgula (os parêntesis são opcionais)

- dicionários:
    - compostos por {chave:valor}
    - não tem índices nem ordem
    - para incluir ou alterar basta chamar a chave: dicio[chave] = valor
    - print(dicio.keys())   -> retorna todas as chaves
    - print(dicio.values()) -> retorna todos os valores
    - print(dicio.items())  -> retorna todos os itens

- funções recursivas: funções que chamam elas mesmas
    (o próximo resultado depende do anterior)
    IMPORTANTE: pensar nas condições de parada

- tratamento de erro (não é apenas capturar/"se livrar" do erro,
    temos que fazer com que o programa continue rodando da melhor forma possível)
    A filosifa é:
        TRY: o código que corre risco de falha
        EXCEPT: o código que roda caso o TRY falhe
        ELSE: o código que roda caso o TRY seja bem sucedido
        FINALLY: o código que sempre roda
'''

#sobre args e kwargs:
# def ola(nome, *args, titulo="Sr.", cidade="São Paulo", Unidade="Paulista", **kwargs):
#     print("-- parametros pré definidos:")
#     print(titulo, cidade, Unidade) #pré-definido
#     print("-- kwargs:")
#     print(type(kwargs))
#     print (kwargs)
#     print("-- args:")
#     print(type(args))
#     print (args)
#     print("-- parametro obrigatório:")
#     print(nome) #obrigatório
#
# ola("Fulano","isto é um *arg",2,"isto também é *args!",cidade="Rio de Janeiro", carro="gol",apto = 300,cor_da_parede = "branca",titulo="Sra.")

'''
1) Crie um programa que permita ao usuário gerenciar uma
lista de compras. O programa deve oferecer um menu de opções e continuar em execução
até que o usuário decida sair, com 4 opções:
- Adicionar item
- Ver lista
- Remover item (aqui, deverá utilizar testes de validação para
não permitir ao usuário remover um item inexistente)
- sair
'''
#primeiro, fazemos um loop infinito com a opção de parar
#depois, implementamos as opções:

lista_de_compras = []  #a lista tem que ser criada fora, para não sobrescrever!!!
while True:

    print("Bem vindo à lojas X. O que deseja?")
    print("1. Adicionar item ao carrinho")
    print("2. Remover item do carrinho")
    print("3. Visualizar lista de compras")
    print("4. sair")
    opcao = input("Por favor, escolha o número da opção desejada: ")
    try:
        opcao = int(opcao)
    except:
        print("Opção inválida! Favor digitar apenas números inteiros!\n")
    else:
        match opcao:
            case 1:
                item = input("Digite o item que deseja comprar: ")
                #podemos numa versão mais elaborada verificar se o item está disponível
                lista_de_compras.append(item)
            case 2:
                item_a_remover = input("Digite o item que deseja remover: ")
                #temos que primeiro verificar se o item existe para não quebrarmos o programa
                if item_a_remover in lista_de_compras:
                    lista_de_compras.remove(item_a_remover) #lembrando que a alteração é na própria lista. Nada é retornado
                    print(f"Item '{item_a_remover}' removido!\n")
                else:
                    print(f"O item '{item_a_remover}' não está no seu carrinho de compras!\n")
            case 3:
                if len(lista_de_compras) != 0:
                    print(f"Você possui {len(lista_de_compras)} item(ns):")
                    for i in lista_de_compras:
                        print ("-", i)
                    print()
                else:
                    print("O carrinho está vazio!!!\n")
            case 4:
                print("Obrigado por visitar nossa loja!")
                break
            case _:
                print("Opção inválida! Escolha um dos números da lista\n")


#EXERCÍCIO: IMPLEMENTE UMA FORMA DE TER VÁRIOS USUÁRIOS!!
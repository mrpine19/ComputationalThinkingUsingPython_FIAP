'''
1) Crie um programa que permita ao usuário gerenciar uma
lista de compras. O programa deve oferecer um menu de opções e continuar em execução
até que o usuário decida sair, com 4 opções:
- Adicionar item
- Ver lista
- Remover item (aqui, deverá utilizar testes de validação para
não permitir ao usuário remover um item inexistente)
- sair

2)Crie um sistema para armazenar e consultar as notas dos alunos utilizando um dicionário,
onde o nome do aluno é a chave e sua nota é o valor.
- Inicie o programa com um dicionário já contendo alguns alunos e suas notas

O programa deve apresentar o seguinte menu ao usuário em um laço contínuo:
1. Consultar nota de aluno
2. Adicionar/Alterar nota de aluno
3. Ver todas as notas
4. Sair

O programa deve pedir o nome de um aluno:
Se o aluno for encontrado, exiba seu nome e sua nota;
Se o aluno não for encontrado (KeyError), exiba uma mensagem de erro apropriada e
pergunte ao usuário se deseja incluir este aluno.

Na opção de adicionar/alterar nota, utilize um try/except para garantir
que a nota inserida seja um valor numérico (ValueError).
Garanta também que seja entre 0 e 10.

'''

def cadastrar_novo_aluno(nome_aluno):

    while True:
        try:
            print("Aluno não encontrado! Deseja cadastrar este aluno?")
            cadastrar_aluno = input("Digite 1 para sim e 2 para não: ")
            cadastrar_aluno = int(cadastrar_aluno)
        except:
            print("Opção inválida! Favor digitar apenas números inteiros!\n")
        else:
            match cadastrar_aluno:
                case 1:
                    notas_alunos.update({nome_aluno: None})
                    print(f"Aluno {nome_aluno} cadastrado no sistema!")
                    break
                case 2:
                    break
                case _:
                    print("Opção inválida! Tente novamente!")

def cadastrar_nota(nome_aluno):
    while True:
        nota_aluno = input(f"A nota atual do aluno {nome_aluno} é {notas_alunos[nome_aluno]}. Digite a nova nota: ")
        try:
            nota_aluno = float(nota_aluno)
        except:
            print("Nota inválida! Favor digitar apenas números!\n")
        else:
            if nota_aluno >= 0 and nota_aluno <= 10:
                notas_alunos[nome_aluno] = nota_aluno
                print(f"A nova nota do aluno {nome_aluno} é {notas_alunos[nome_aluno]}.\n")
                break
            else:
                print("Nota inválida! Digite uma nota maior ou igual a 0 e menor ou igual a 10!\n")


notas_alunos = {
    "Ana": 8.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8,
    "Mariana": 10.0
}
while True:

    print("Bem vindo ao Sitema de Professores da FIAP. O que deseja?")
    print("1. Consultar nota de aluno")
    print("2. Adicionar/Alterar nota de aluno")
    print("3. Ver todas as notas")
    print("4. sair")
    opcao = input("Por favor, escolha o número da opção desejada: ")
    print()

    try:
        opcao = int(opcao)
    except:
        print("Opção inválida! Favor digitar apenas números inteiros!\n")
    else:
        match opcao:
            case 1:
                nome_aluno = input("Digite o nome do aluno: ")

                if nome_aluno in notas_alunos:
                    print(f"A nota do {nome_aluno} é {notas_alunos[nome_aluno]}")
                else:
                    cadastrar_novo_aluno(nome_aluno)
                print()
            case 2:
                nome_aluno = input("Qual aluno você quer alterar a nota? ")
                if nome_aluno in notas_alunos:
                    cadastrar_nota(nome_aluno)
                else:
                    cadastrar_novo_aluno(nome_aluno)
            case 3:
                for aluno in notas_alunos:
                    print(f"A nota do aluno {aluno} é {notas_alunos[aluno]}.")
                print()
            case 4:
                print("Encerrando o programa...")
                break
            case _:
                print("Número inválido. Tente novamente.\n")
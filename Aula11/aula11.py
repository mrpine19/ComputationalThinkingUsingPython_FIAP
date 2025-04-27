## LOOPs infinitos

#lembrando que uma comparação no python é respondida com uma Booleana (True ou False),
#e que o while (enquanto) ele funciona ENQUANTO a pergunta for True,
# a forma de eu colocar um loop para ser eterno é...
'''contador = 1 # tiramos do 0 por uma decisão de negócios de não ter senha 0
while True: #isto é um loop infinito, pois eu mando ele executar enquanto a
            #verdade for verdadeira
    if contador > 999:
        contador = 1
    print("Senha numero", contador,"favor comparecer ao balcão!")
    contador += 1'''


### BREAK, CONTINUE, PASS

##BREAK -> quebrar
#é usado para PARAR o loop
senha = 0
#vamos supor que só temos 8000 no estoque,
# então temos que PARAR o loop ao esotque zerar
'''estoque = 8000 #vamos supor que a quantidade de estoque venha por meio de uma API
botao_aposentar_apertado = False #supondo que venha por um botão de ganhar na mega sena
while True: #isto é um loop infinito, pois eu mando ele executar enquanto a
            #verdade for verdadeira
    if senha > 999: #independentemente da quantidade do meu estoque, meu mostrador
                    #continua indo apenas até 999
        senha = 1
    if estoque == 0: #caso o estoque acabe, eu tenho que para de chamar senhas!
        break #quebro o meu loop
    if botao_aposentar_apertado == True:#caso eu decida parar, o loop para
        break
    print("Senha numero", senha, "favor comparecer ao balcão!")
    senha += 1'''


#também funciona com o FOR:
'''for i in range(8000): #quando eu não defino, o start é 0 e o step é 1
                        #isto é equivalente a range(0,8000,1)
    print("Senha numero", senha, "favor comparecer ao balcão!")
    if botao_aposentar_apertado == True:
        break #aqui,caso algo faça o status do botão mudar para apertado, para oloop
                #independentemente de qual seja o valor do 'i'
'''
## PASS (passe) -> não faz nada!
'''for i in range(101):
    if i%2 == 0: #se for par
        pass #não faz nada, mas também não dá erro
                #é uma forma de conseguir fazer o programa rodar enquanto
                #não se tem uma definição.
                #Também é uma forma de deixar o código explícito
    else:
        print(i)'''

## CONTINUE: volta para o começo do loop (e no caso do FOR, avança a contagem)
'''for i in range(5):
    if idade > 65:
        continue #aqui, eu joguei o código de volta para o começo do loop,
                #ignorando o que vem abaixo
    cobro_passagem()'''

##Como utilizar um loop para forçar o usuário a ecolher um número da forma
# que a gente quiser (inteiro, par, itens do menu, etc....)?

#Vamos simular para forçar o usuário a digitar um número menor que 10:
numero = float(input("Por favor digite um número menor do que 10: "))
while numero >= 10: #eu quero que ele repita ENQUANTO estiver ERRADO
                    #eu tenho que colocar na 'pergunta' do while, tudo que eu
                    #NÃO QUERO
    print("Erro! Por favor, se atente aos requisitos!")
    numero = float(input("Por favor digite um número menor do que 10: "))
print(f"Obrigado!\nNúmero {numero} registrado!")


##############################################################
#EXERCÍCIOS:


# 1) Solicite dois número ao usuário, sendo que o segundo deverá ser obrigatoriamente maior que o primeiro

# 2) Solicitar um número obrigatoriamente inteiro positivo do usuário, e calcular seu fatorial

# 3) faça um programa que imprima a soma dos números inteiros positivos de 1 a 100, inclusive
# faça este exercício uma vez utilizando o for, e outra utilizando o while

# 4) imprima a tabuada do número 5, entre 0 e 10, inclusive, tanto utiliando o for quanto o while
# Depois, adapte o programa para receber dois números do usuário: o de início e o de fim
# faça este exercício uma vez utilizando o for, e outra utilizando o while

# 5) solicite 2 números ao usuário. Para cada número do 1 ao primeiro número, faça a tabuada dele do 0 até o segundo número

# 6) faça um programa que solicite ao usuário um número N obrigatoriamente inteiro entre 1 e 20
# este número N vai ser a quantidade de novos números a serem digitados pelo usuário
# ao terminar de digitar estes N números, o programa deverá imprimir:
# ## o maior valor
# ## o menor valor
# ## a soma de todos os valores
# ## a média de todos os valores
# ## quantos porcento dos valores foram positivos
# ## quantos porcento dos valores foram negativos

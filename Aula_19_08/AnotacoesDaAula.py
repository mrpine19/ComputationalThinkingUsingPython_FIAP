#faça um script que, enquanto uma pessoa digitar um input que não seja um número inteiro
#force o usuário a tentar novamente

def numero_inteiro():
    try:
        numero_digitado = int(input("Digite um número: "))

    except:
        print(f"Você não digitou um número inteiro. Tente novamente.\n")
        return numero_inteiro()
    else:
        return numero_digitado

numero = numero_inteiro()
print(f"O número digitado foi {numero}")
lista = [[1, 2, 3], ["gato", "cachorro", "Camelo", "Leopardo"], 3, "Opa", [4, 5]]

print(type(lista))

for elemento in lista:
    if type(elemento) == list:
        print(f"O item '{elemento}' é uma lista e possui {len(elemento)} itens dentro dela.")
        if len(elemento) >= 3:
            print(f"O terceiro elemento dessa lista é '{elemento[2]}'.")
    else:
        print(f"O item '{elemento}' não é uma lista.")

    print("--------------------")

# 5) solicite 2 números ao usuário. Para cada número do 1 ao primeiro número, faça a tabuada dele do 0 até o segundo número

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

for i in range(1, num1 + 1):
    print("------------------------------------")
    for j in range(0, num2 + 1):
        print(f"{i} * {j} = {i * j}")
    print("------------------------------------")
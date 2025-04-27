# 1) Solicite dois número ao usuário, sendo que o segundo deverá ser obrigatoriamente maior que o primeiro
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número. Este deve ser maior que o primeiro número digitado: "))

while num1 > num2:
    num2 = int(input("O número digitado não é válido. Digite novamente: "))

print(f"Os números digitados são: {num1}, {num2}")
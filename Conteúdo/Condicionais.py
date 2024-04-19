'''
Condicionais em python:

if = se
else = senão (Usado na última opção, geralmente no "sair do app")
elif = então (junção de if e else)

'''


print("Digite seu nome: ")
nome = input()

print("Digite sua idade: ")
idade = int(input())


if idade < 18:
        print("Você é menor de idade!!")
if idade > 18:
        print("Você é maior de idade!!")

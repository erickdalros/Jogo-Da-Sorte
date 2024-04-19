'''
Existem alguns tipos de dados de entrada e saída:

1 - Tipo numérico
2 - Tipo float
3 - Tipo Booleano
4 - Escopo de variáveis

'''


# TIPO NUMÉRICO (Soma, subtração, divisão, multiplicação e resto da divisão)
print(5 + 4 - 2 / 10 * 10 % 20)

# TIPO FLOAT (Decimal, Inteiro, Real)

valor = 1
nome = "Erick"
valor_dois = 1.232

print(type(valor)) # Aqui conseguimos ver ual o tipo float do valor da variável
print(type(nome)) # Aqui conseguimos ver ual o tipo float do valor da variável
print(type(valor_dois)) # Aqui conseguimos ver ual o tipo float do valor da variável

# TIPO BOOLANO (True ou False)

print(input("Digite o código: "))

alpha = True
print(alpha)
beta = False
print(beta)

# ESCOPO DE VARIÁVEIS

print(input("Digite o código de acesso: "))

codigo = 10

if codigo == 10:
    print("Acesso Liberado")
else:
    print("Acesso negado")





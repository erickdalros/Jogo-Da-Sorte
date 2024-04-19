import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 5

    while tentativas < max_tentativas:
        tentativa = int(input("Digite um número entre 1 e 100: "))

        if tentativa == numero_secreto:
            print("Parabéns! Você acertou o número.")
            return  # Retorna da função, encerrando o jogo
        elif tentativa < numero_secreto:
            print("O número que você digitou é menor.")
        else:
            print("O número que você digitou é maior.")

        tentativas += 1
        tentativas_restantes = max_tentativas - tentativas
        print(f"Tentativas restantes: {tentativas_restantes}")

    print(f"Suas {max_tentativas} tentativas acabaram. O número era {numero_secreto}.")

# Exemplo de uso da função
jogo_adivinhacao()

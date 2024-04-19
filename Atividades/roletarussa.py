#GERAÇÃO DE NÚMEROS ALEATÓRIOS
import random
# PONTOS DE FASES
pontos = 0





def fase_um():
    numero_cpu = random.randint(1, 2)
    tentativas = 0
    max_tentativas = 5
    

    while tentativas < max_tentativas: # Para confirmar que não excedeu o máximo de tentativas
        tentativa = int(input("Digite um número entre 1 e 100: ")) #Entrada do valor do usuário

        if tentativa == numero_cpu:  # CASO DE ACERTO NO CHUTE
            print("OK, Você me ganhou nessa, porém vamos brincar mais heheheh") 
            return # O RETURN TEM QUE SER AQUI, POIS CASO ELE GANHE O GAME, ELE EXECUTARÁ O JOGO DOIS
            
        elif tentativa < numero_cpu: # EM CASO DE ERRO NO CHUTE
            print("Errou!!!!!!!")
        



        # CALCULO DE QUANTAS TENTATIVAS TEM AINDA
        tentativas_restantes = max_tentativas - tentativas
        print(f"Tentativas restantes: {tentativas_restantes}")




fase_um() # Fecha aqui a função fase_um


print("Jogo dois")








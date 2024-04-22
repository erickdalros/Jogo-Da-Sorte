#GERAÇÃO DE NÚMEROS ALEATÓRIOS
import random
# PONTOS DE FASES

# CADASTRO SIMPLES DE USER
print("Digite seu user: ")
user = input()
print("Digite sua Senha: ")
senha = input()
print(f'Seja bem vindo(a) {user}, lebre-se que sua senha é {senha}')

print("Antes de iniciar o game, leia as regras: ")
print(
      '[1] - Esse jogo é apenas um representação não ofensiva de como é o jogo RELETA RUSSA\n'
      '[2] - Não incentivamos ninguém a jogar o na vida real, caso você queira isso não é responsabilidade nossa, PROCURE AJUDA\n'
      '[3] - Você tem ao todo apenas 5 tentativas, caso você perca as cinco, deve-se então reiniciar o jogo\n'
      '[4] - Divirta-se e nos siga no github para mais jogos: https://github.com/erickdalros \n'
      )

# INÍCIO DA FASE UM
def fase_um():
    numero_cpu = random.randint(1, 5)
    tentativas = 0
    max_tentativas = 5
    

    while tentativas < max_tentativas: # Para confirmar que não excedeu o máximo de tentativas
        tentativa = int(input("Digite um número entre 1 e 100: ")) #Entrada do valor do usuário

        if tentativa == numero_cpu:  # CASO DE ACERTO NO CHUTE
            print("OK, Você me ganhou nessa, porém vamos brincar mais heheheh") 
            return # O RETURN TEM QUE SER AQUI, POIS CASO ELE GANHE O GAME, ELE EXECUTARÁ O JOGO DOIS
            
        elif tentativa != numero_cpu: # EM CASO DE ERRO NO CHUTE
            print("Errou!!!!!!!")
        
        # CALCULO DE QUANTAS TENTATIVAS TEM AINDA
        tentativas += 1  # Incrementa as tentativas após um chute errado
        tentativas_restantes = max_tentativas - tentativas        
        print(f"Tentativas restantes: {tentativas_restantes}")

fase_um() # Fecha aqui a função fase_um

def fase_dois():
    print("")
    
    # FAZER TODA A LÓGICA DA PARTE DOIS, VERIFICAR SE AO CRIAR OUTRA FUNÇÃO AS TENTATIVAS ANTERIORES SERÃO SALVAS OU IRÁ REINICIAR DNV (LEIA AS REGRASPARA SABER OQ FAZER ) GRAXA VEIA

fase_dois()









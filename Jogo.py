#Jogo Jokenpo

#Importando a biblioteca
import random

#Iniciando a estrutura de condição
while True:

    escolhas =['pedra','papel','tesoura']
    computador = random.choice(escolhas)#Escolha aleatoria
    jogador = None #None=nada

#Pediando ao usuario para escolher
    while jogador not in escolhas:
        #Pedindo p/o usúario escolher
        jogador = input("pedra,papel ou tesoura? ").lower()# converte p/minúsculas

    if jogador ==  computador:
        print("Computador: "+ computador)
        print("Jogador: "+jogador)
        print("Empate!!")
#Condição  de sequência

    elif jogador == "pedra":
        if computador == "papel":
            print("Computador: " + computador)
            print("Jogador: " + jogador)
            print("Você perdeu!!")

        elif computador == "tesoura":
            if computador == "papel":
                print("Computador: " + computador)
                print("Jogador: " + jogador)
                print("Você ganhou!!")

            elif jogador == "tesoura":
                if computador == "pedra":
                    print("Computador: " + computador)
                    print("Jogador: " + jogador)
                    print("Você perde!!")

                elif computador == "papel":
                    if  computador == "pedra":
                        print("Computador: " + computador)
                        print("Jogador: " + jogador)
                        print("Você ganhou!!")

                    elif jogador == "papel":
                        if computador == "tesoura":
                            print("Computador: " + computador)
                            print("Jogador: " + jogador)
                            print("Você perdeu!!")

                        elif computador == "tesoura":
                                print("Computador: " + computador)
                                print("Jogador: " + jogador)
                                print("Você ganhou!!")
        jogador_novamente = input("Voce quer jogar novamente? (s/n): ").lower()

        if jogador_novamente != "s":
            print("Obrigada por jogar!")

            break
            

import random


def jogar():
    print("*******************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("********************************")

    numero_secreto = random.randrange(1, 101)

    total_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativas {} de {} ".format(rodada, total_tentativas))

        chute_string = input("Digite um numero entre 1 e 100: ")
        print("Você digitou ", chute_string)
        chute = int(chute_string)

        if chute < 1 or chute > 100:
            print("Você deve digitar entre 1 e 100!")
            continue

        acertou = numero_secreto == int(chute)
        maior = int(chute) > numero_secreto
        menor = int(chute) < numero_secreto

        if acertou:
            print("Pararéns você acertou e fez {} pontos".format(pontos))
            break
        else:

            if maior:
                print("Você errou miseravelmente seu numero for MAIOR que o numero secreto!")
            elif menor:
                print("Você errou miseravelmente seu numero for MENOR que o numero secreto!")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo numero secreto:", numero_secreto)


if __name__ == "__main__":
    jogar()

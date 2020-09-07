import random


def jogar():
    mensagem_abertura()

    palavra_secreta = carregar_palavra_secreta()

    letras_encontradas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_encontradas)

    while not enforcou and not acertou:

        chute = carrega_chute()

        if chute in palavra_secreta:
            letras_encontradas = define_chute_correto(palavra_secreta, letras_encontradas, chute)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_encontradas

        print(letras_encontradas)

        print("Jogando...")

    if acertou:
        mensagem_vitoria()
    else:
        mensagem_derrota(palavra_secreta)

    print("Fim do jogo palavra secreta:", palavra_secreta)


if __name__ == "__main__":
    jogar()


def mensagem_abertura():
    print("*******************************")
    print("***Bem vindo ao jogo forca!****")
    print("*******************************")


def carregar_palavra_secreta():
    arquivo = open("./palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip().upper())

    arquivo.close()

    return palavras[random.randrange(0, len(palavras))]


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def carrega_chute():
    chute = input("Qual letra? ")
    return chute.strip().upper()


def define_chute_correto(palavra_secreta, letras_encontradas, chute):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_encontradas[index] = chute
        index += 1
    return letras_encontradas


def mensagem_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
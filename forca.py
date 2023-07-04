import random


def jogar():

    mensagem_deabertura()
    palavra_secreta = carregar_palavra_secreta()
    chances = dificuldade_do_jogo()

    letras_acertadas = ini_letras_acertadas(palavra_secreta)
    print(''.join(letras_acertadas))

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in palavra_secreta:
            letras_acertadas = ver_letras_acertadas(palavra_secreta, chute, letras_acertadas)
        else:
            chances = chances-1
            print("Você tem {} chances".format(chances))
            desenha_forca(7-chances)

        enforcou = chances == 0
        acertou = '_' not in letras_acertadas
        print(''.join(letras_acertadas))

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")


def mensagem_deabertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carregar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def ini_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    return input("Digite o seu chute: ").strip().upper()


def ver_letras_acertadas(palavra, chute, acertadas):
    # Loop para comparar cada letra da palavra secreta com o chute
    index = 0
    for letra in palavra:
        if letra == chute:
            acertadas[index] = letra
        index += 1
    return acertadas


def imprime_mensagem_vencedor():

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
    print("Imagine que caiu uma chuva de confetes, agora vá embora...Tchau!")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Você errou, a palavra era {} "
          "talvez seja melhor ler um livro "
          "e aprender palavras novas".format(palavra_secreta))
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

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
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


def dificuldade_do_jogo():
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_de_tentativas = 7
    elif nivel == 2:
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3
    return total_de_tentativas


if __name__ == "__main__":
    jogar()

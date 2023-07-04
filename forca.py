import random


def jogar():

    mensagem_deabertura()
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = ini_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    chances = 5

    # Laço de repetição não para até que o jogador perca ou acerte a palavra
    while not enforcou and not acertou:
        chute = input("Digite o seu chute: ").strip().upper()
        index = 0

        if chute in palavra_secreta:
            # Loop para comparar cada letra da palavra secreta com o chute
            for letra in palavra_secreta:
                if letra == chute:
                    letras_acertadas[index] = letra
                index += 1
            if ''.join(letras_acertadas).find('_') < 0:
                acertou = True
                print("Você acertou!!! Imagine que caiu uma chuva de confetes, agora vá embora")
            print(''.join(letras_acertadas))
        else:
            chances = chances-1
            if chances == 0:
                enforcou = True
                print("Você errou, a palavra era {} "
                      "talvez seja melhor ler um livro "
                      "e aprender palavras novas".format(palavra_secreta))
            else:
                # Imprime como está o estado atual da palavra
                print(''.join(letras_acertadas))
                print("Você tem {} chances".format(chances))
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


if __name__ == "__main__":
    jogar()

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "Renato"
    palavra_secreta = palavra_secreta.upper()
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    enforcou = False
    acertou = False
    chances = 5
    while not enforcou and not acertou:
        chute = input("Digite o seu chute: ").strip().upper()
        index = 0
        for letra in palavra_secreta:
            if letra.upper() == chute:
                letras_acertadas[index] = letra.upper()
            index = index + 1
        print(''.join(letras_acertadas))
        if palavra_secreta.find(chute) < 0:
            chances = chances-1
            if chances == 0:
                enforcou = True
                print("Você errou, talvez seja melhor ler um livro e aprender palavras novas")
        if ''.join(letras_acertadas).find('_') < 0:
            acertou = True
            print("Você acertou!!!")
        #if chute == palavra_secreta:
        #    acertou = True
        #    print("Parabéns você acertou")
        #else:
        #    chances = chances-1
        #    if chances == 0:
        #        enforcou = True
        #
        #    else:
        #        print("Continue jogando...")
    print("Fim do jogo")


if __name__ == "__main__":
    jogar()

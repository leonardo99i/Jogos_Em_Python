import random
def jogar():
    print("****************************")
    print("********Jogo de Forca*******")
    print("****************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    enforcou = False
    acertou = False
    erros = 0
    print(letras_acertadas)

    #Enquanto (True)
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0

            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você Acertou, era {}".format(palavra_secreta))
    else:
        print("Você Perdeu, a palavra era {}".format(palavra_secreta))

    print("FIM DO JOGO")
if(__name__ == "__main__"):
    jogar()
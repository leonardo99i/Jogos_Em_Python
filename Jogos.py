import Forca
import Advinhacao

def escolhe_jogo():
    print("****************************")
    print("******Escolha seu jogo******")
    print("****************************")

    print("(1) - Forca  (2) - Adivinhação")

    jogo = int (input("Qual jogo vc vai jogar: "))

    if(jogo == 1):
        print("Jogo da forca")
        Forca.jogar()
    elif(jogo == 2):
        print("Jogo da advinhação")
        Advinhacao.jogar()
    
if(__name__ == "__main__"):
    escolhe_jogo()
    
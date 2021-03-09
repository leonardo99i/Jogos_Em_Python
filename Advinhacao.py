def jogar():
    import random
    print("****************************")
    print("*****Jogo de Advinhação*****")
    print("****************************")

    numero_sorteado = random.randrange(1,101) #Numero sorteado aleatoriamente entre 1 a 100 
    total_de_tentativas = 0 #Numero de tentativas que eu determinei
    pontos = 1000 #Numero de pontos que diminue conforme vc erra

    print("Escolha um nível de dificuldade: ")
    print("(1) - Fácil  (2) - Médio  (3) - Difícil")
    nivel = int (input("Escolha um nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1): #A função range funciona com os seguintes parametros range(start,stop, step). step é opcional, como por exemplo 3 se queremos pular de 3 em 3 começando do start 1 e um stop de 10.
        print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #String Interpolation
        chute_str = input("Digite um número entre 1 e 100: ")#Entrada para o usuario digitar seu chute
        print("Você digitou", chute_str) #Imprimir o que o usuario digitou 
        chute = int(chute_str) #Convertendo uma String em inteiro, pode ser declarado de outra forma tbm chute = int(input("Texto do input")), assim não prescisando converter

        if(chute < 1 or chute > 100):
            print("Por Favor, digite um número entre 1 e 100.")
            continue

        acertou = chute == numero_sorteado
        maior = chute > numero_sorteado
        menor = chute < numero_sorteado

        #Loop até acertar, dentro do limite das rodadas e Comparação para saber se acertou ou errou
        if(acertou):
            print("Parabens!!! Você Acertou")
            print("Você fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Você Errou, o seu chute foi maior que o número sorteado.")
            
            elif(menor):
                print("Você Errou, o seu chute foi menor que o número sorteado.")
            pontos_perdidos = abs(numero_sorteado - chute) #Ex: 40 - 20 = 20 pontod perdidos
            pontos = pontos - pontos_perdidos


    print("Fim de jogo, o número era {}".format(numero_sorteado))

if(__name__ == "__main__"):
    jogar()

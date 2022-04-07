print("*********************")
print("**** Bem Vindo! *****")
print("*********************")

numero_secreto = 31
total_de_tentativas = 3
for rodada in range(1, total_de_tentativas + 1):
    chute = int(input("\nDigite um número: "))
    print("\nvocê digitou", chute)

    acertou = numero_secreto == chute
    maior   = chute>numero_secreto
    menor   = chute<numero_secreto

    if (acertou):
        print("você acertou!")
    else:
        if (maior):
            print("você errou! Seu número foi maior que o numero secreto.")
        elif (menor):
            print("você errou! Seu número foi menor que o numero secreto.")
print("\n>>>> Fim de Jogo! <<<<")
    
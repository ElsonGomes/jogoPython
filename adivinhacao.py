import random
print("*********************")
print("**** Bem Vindo! *****")
print("*********************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 3
pontos = 1000

print("Qual o nivel de dificuldade")
print("(1) Facil (2) Medio (3) Dificil")
while(True):
    nivel = int(input("Defina o nivel: "))

    if(nivel==1):
        total_de_tentativas = 10
        break
    elif(nivel==2):
        total_de_tentativas = 5
        break
    elif(nivel==3):
        total_de_tentativas = 3
        break
    else:
        print("Nivel incorreto\n")
        True


for rodada in range(1, total_de_tentativas + 1):
    print(f"\nTentativa {rodada} de {total_de_tentativas}")
    chute = int(input("\nDigite um número entre (1 e 100): "))
    print("\nvocê digitou", chute)
    if(chute<1 or chute>100):
        print("Voce digitou um numero errado, o numero deve ser entre (1 e 100)")
        continue
    if(chute):
        acertou = numero_secreto == chute
        maior   = chute>numero_secreto
        menor   = chute<numero_secreto

        if (acertou):
            print(f"você acertou! e fez {pontos}")
            break
        else:
            if (maior):
                print("você errou! Seu número foi maior que o numero secreto.")
            elif (menor):
                print("você errou! Seu número foi menor que o numero secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
print("\n>>>> Fim de Jogo! <<<<")
    
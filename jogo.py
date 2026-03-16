import random # Requisito 5: Uso da biblioteca random 

def jogar_jokenpo():
    print("--- DESAFIO: PEDRA, PAPEL OU TESOURA ---")
    
    # Requisito 1: Variáveis 
    opcoes = ["pedra", "papel", "tesoura"]
    continuar = "s"

    # Requisito 4: Estrutura de repetição 
    while continuar.lower() == "s":
        # Requisito 5: Uso da biblioteca random para a escolha da máquina 
        computador = random.choice(opcoes)
        
        print("\nEscolha sua jogada: pedra, papel ou tesoura")
        # Requisito 2: Entrada de dados com input() 
        jogador = input("Sua escolha: ").lower()

        if jogador not in opcoes:
            print("Escolha inválida! Tente novamente.")
            continue

        print(f"O computador escolheu: {computador}")

        # Requisito 3: Estrutura condicional (if/else) para verificar o resultado 
        if jogador == computador:
            print("Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or \
             (jogador == "papel" and computador == "pedra") or \
             (jogador == "tesoura" and computador == "papel"):
            # Requisito 6: Mensagem de vitória 
            print("VOCÊ VENCEU! Parabéns.")
        else:
            # Requisito 6: Mensagem de derrota 
            print("VOCÊ PERDEU! Mais sorte na próxima.")

        continuar = input("\nDeseja jogar novamente? (s/n): ")

    print("\nObrigado por jogar!")

# Executar o jogo
jogar_jokenpo()
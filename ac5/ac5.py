"""
Programação Estruturada
2024.1
15/03/2024

AC5
"""
from random import randint

def main():
    # Atributos do aventureiro
    vida_aventureiro = 100
    ataque_aventureiro = randint(10, 20)
    defesa_aventureiro = randint(1, 5)

    # Atributos do monstro
    vida_monstro = randint(60, 80)
    ataque_monstro = randint(20, 30)

    print("Atributos iniciais:")
    print("Aventureiro -> Vida:",vida_aventureiro,", Ataque:",ataque_aventureiro,", Defesa:",defesa_aventureiro)
    print("Monstro -> Vida:",vida_monstro,", Ataque:",ataque_monstro)

    rodada = 1
    while vida_aventureiro > 0 and vida_monstro > 0:
        print("\nRodada",rodada,":")
        
        # Aventureiro ataca o monstro
        dano_ataque_aventureiro = randint(1, ataque_aventureiro)
        vida_monstro -= dano_ataque_aventureiro
        if vida_monstro <= 0:
            print("O monstro morreu!")
            break
        print("O aventureiro ataca o monstro, causando",dano_ataque_aventureiro,"de dano. Vida do monstro:",vida_monstro)

        # Monstro ataca o aventureiro
        dano_ataque_monstro = randint(1, ataque_monstro) - defesa_aventureiro
        if dano_ataque_monstro < 0:
            dano_ataque_monstro = 0
        vida_aventureiro -= dano_ataque_monstro
        if vida_aventureiro <= 0:
            print("O aventureiro morreu!")
            break
        print("O monstro ataca o aventureiro, causando",dano_ataque_monstro,"de dano. Vida do aventureiro:",vida_aventureiro)

        rodada += 1

    print("\nAtributos finais:")
    print("Aventureiro -> Vida:",vida_aventureiro,", Ataque:",ataque_aventureiro,", Defesa:",defesa_aventureiro)
    print("Monstro -> Vida:",vida_monstro,", Ataque:",ataque_monstro)

if __name__ == "__main__":
    main()










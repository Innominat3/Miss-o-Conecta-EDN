def exercicio_2():
    print("\n" + "="*50)
    print("EXERCÍCIO 2 - Ano de Nascimento")
    print("="*50)

    ANO_ATUAL = 2026

    nome = input("Digite seu nome: ").strip()
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    idade = ANO_ATUAL - ano_nascimento

    print(f"\n{nome}, você tem {idade} anos.")


if __name__ == "__main__":
    exercicio_2()

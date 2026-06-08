def exercicio_4():
    print("\n" + "="*50)
    print("EXERCÍCIO 4 - Número Par ou Ímpar")
    print("="*50)

    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        print(f"O número {numero} é PAR.")
    else:
        print(f"O número {numero} é ÍMPAR.")


if __name__ == "__main__":
    exercicio_4()

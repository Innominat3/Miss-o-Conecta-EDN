def exercicio_5():
    print("\n" + "="*50)
    print("EXERCÍCIO 5 - Divisão Inteira e Resto")
    print("="*50)

    numero_1 = int(input("Digite o primeiro número: "))
    numero_2 = int(input("Digite o segundo número: "))

    if numero_2 != 0:
        divisao_inteira = numero_1 // numero_2
        resto = numero_1 % numero_2

        print("\n--- Resultado da Divisão ---")
        print(f"Divisão inteira: {divisao_inteira}")
        print(f"Resto da divisão: {resto}")
    else:
        print("Não é possível dividir p/0.")


if __name__ == "__main__":
    exercicio_5()

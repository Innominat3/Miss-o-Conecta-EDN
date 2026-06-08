def exercicio_3():
    print("\n" + "="*50)
    print("EXERCÍCIO 3 - Calculadora com Input")
    print("="*50)

    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))

    print("\n--- Resultados ---")
    print(f"Soma:          {numero_1 + numero_2}")
    print(f"Subtração:     {numero_1 - numero_2}")
    print(f"Multiplicação: {numero_1 * numero_2}")

    if numero_2 != 0:
        print(f"Divisão:       {numero_1 / numero_2:.2f}")
    else:
        print("Divisão:       Não é possível dividir por zero.")


if __name__ == "__main__":
    exercicio_3()

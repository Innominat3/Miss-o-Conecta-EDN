def exercicio_1():
    print("\n" + "="*50)
    print("EXERCÍCIO 1 - Cadastro Interativo")
    print("="*50)

    nome = input("Digite o nome do aluno: ").strip()
    idade = int(input("Digite a idade: "))
    matriculado_input = input("Está matriculado? (sim/não): ").strip().lower()
    
    matriculado = matriculado_input in ["sim", "s", "true", "1"]

    print("\n--- Cadastro do Aluno ---")
    print(f"Nome:        {nome}")
    print(f"Idade:       {idade} anos")
    print(f"Matriculado: {'Sim' if matriculado else 'Não'}")


if __name__ == "__main__":
    exercicio_1()

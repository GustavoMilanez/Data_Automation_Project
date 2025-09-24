def registrar_testes_transformadores(qtd):
    transformadores_aprovados = []

    for i in range(1, qtd + 1):
        codigo = f"T{i:04d}"  # Ex: T0001, T0002, ...
        print(f"\nRegistrando transformador {codigo}:")

        resultado_hi_pot = input("Passou no teste Hi Pot? (s/n): ").strip().lower()
        if resultado_hi_pot != 's':
            print(f"{codigo} reprovado no teste Hi Pot.")
            continue

        resultado_giga = input("Passou no teste Giga? (s/n): ").strip().lower()
        if resultado_giga != 's':
            print(f"{codigo} reprovado no teste Giga.")
            continue

        # Se passou nos dois testes, é registrado
        transformadores_aprovados.append(codigo)
        print(f"{codigo} aprovado nos dois testes!")

    print("\nResumo final:")
    print(f"Total testado: {qtd}")
    print(f"Aprovados nos dois testes: {len(transformadores_aprovados)}")
    print("Códigos aprovados:", transformadores_aprovados)

# Simula o início do processo
qtd_total = int(input("Quantos transformadores deseja registrar? "))
registrar_testes_transformadores(qtd_total)
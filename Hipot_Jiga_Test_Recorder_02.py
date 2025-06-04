# Dicionário com todos os códigos de barras gerados no início do dia
# Nenhum transformador possui testes feitos inicialmente
transformadores = {
    "T001": {"HiPot": "", "Giga": ""},
    "T002": {"HiPot": "", "Giga": ""},
    "T003": {"HiPot": "", "Giga": ""},
    "T004": {"HiPot": "", "Giga": ""},
    "T005": {"HiPot": "", "Giga": ""},
}

print("=== SISTEMA DE RASTREABILIDADE - TESTES DE TRANSFORMADORES ===")
print("Use o leitor para bipar o código de barras.\n")

while True:
    codigo = input("Bipar código de barras (ou digite 'fim' para encerrar): ").strip().upper()
    
    if codigo == 'FIM':
        break

    if codigo in transformadores:
        print(f"\nCódigo reconhecido: {codigo}")
        
        # Teste de Hi Pot
        if transformadores[codigo]["HiPot"] == "":
            resultado_hipot = input("Resultado do teste Hi Pot (Aprovado / Reprovado): ").strip().capitalize()
            transformadores[codigo]["HiPot"] = resultado_hipot
        else:
            print("Teste Hi Pot já registrado. Substituindo resultado...")
            resultado_hipot = input("Novo resultado do teste Hi Pot: ").strip().capitalize()
            transformadores[codigo]["HiPot"] = resultado_hipot

        # Teste de Giga
        if transformadores[codigo]["Giga"] == "":
            resultado_giga = input("Resultado do teste Giga (Aprovado / Reprovado): ").strip().capitalize()
            transformadores[codigo]["Giga"] = resultado_giga
        else:
            print("Teste Giga já registrado. Substituindo resultado...")
            resultado_giga = input("Novo resultado do teste Giga: ").strip().capitalize()
            transformadores[codigo]["Giga"] = resultado_giga

    else:
        print("Código de barras não encontrado no sistema. Verifique com o supervisor.\n")

# RESUMO FINAL
print("\n=== RELATÓRIO FINAL DO DIA ===")
print(f"{'Código':<10} {'HiPot':<15} {'Giga':<15}")
print("-" * 40)
for cod, testes in transformadores.items():
    print(f"{cod:<10} {testes['HiPot']:<15} {testes['Giga']:<15}")
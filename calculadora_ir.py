def calcular_imposto_renda(renda, dependentes):
    # Tabela de alíquotas do IR para o ano base (2023)
    faixas = [
        (22847.76, 0.0),
        (33919.80, 0.075),
        (45012.60, 0.15),
        (55976.16, 0.225),
        (float('inf'), 0.275)
    ]

    # Dedução por dependente
    deducao_dependente = 289.59
    deducao_total = dependentes * deducao_dependente

    # Base de cálculo
    base_calculo = renda - deducao_total

    # Cálculo do imposto
    if base_calculo <= 0:
        return 0.0

    imposto = 0.0
    for i in range(len(faixas)):
        limite_inferior = 0 if i == 0 else faixas[i - 1][0]
        limite_superior = faixas[i][0]
        aliquota = faixas[i][1]

        if base_calculo > limite_superior:
            imposto += (limite_superior - limite_inferior) * aliquota
        else:
            imposto += (base_calculo - limite_inferior) * aliquota
            break

    return imposto

def main():
    print("Calculadora de Imposto de Renda - Brasil 2023")
    try:
        renda = float(input("Informe sua renda anual (em R$): "))
        dependentes = int(input("Informe o número de dependentes: "))
    except ValueError:
        print("Por favor, insira valores válidos.")
        return

    imposto_devido = calcular_imposto_renda(renda, dependentes)
    
    print("\n----- Relatório de Imposto de Renda -----")
    print(f"Renda Anual: R$ {renda:.2f}")
    print(f"Número de Dependentes: {dependentes}")
    print(f"Imposto Devido: R$ {imposto_devido:.2f}")
    print("------------------------------------------")

if __name__ == "__main__":
    main()

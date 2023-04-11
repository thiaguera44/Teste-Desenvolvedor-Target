def calcular_faturamento(vetor):
    # menor valor de faturamento
    menor = vetor[0]
    for valor in vetor:
        if valor < menor:
            menor = valor

    # maior valor de faturamento
    maior = vetor[0]
    for valor in vetor:
        if valor > maior:
            maior = valor

    # média mensal de faturamento
    media = sum(vetor) / len(vetor)
    print(f"\33[32mMédia mensal de faturamento: R${media:.2f}\33[m")

    # número de dias em que o faturamento diário foi superior à média mensal
    dias_acima = 0
    for valor in vetor:
        if valor > media:
            dias_acima += 1

    return menor, maior, dias_acima

# exemplo de uso
print('=-'*30)
faturamento_diario = [100, 150, 80, 200, 120, 90, 180, 160, 110, 130, 170, 140]
menor, maior, dias_acima = calcular_faturamento(faturamento_diario)
print(f"Menor faturamento diário: R${menor:.2f}")
print(f"Maior faturamento diário: R${maior:.2f}")
print(f"Foram {dias_acima} dias com faturamento acima da média mensal.")

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
faturamento_diario = [22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0, 42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 3847.4823, 373.7838, 2659.7563, 48924.2448, 
                     18419.2614, 0.0, 0.0, 35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495, 8414.61]
menor, maior, dias_acima = calcular_faturamento(faturamento_diario)
print(f"Menor faturamento diário: R${menor:.2f}")
print(f"Maior faturamento diário: R${maior:.2f}")
print(f"Foram {dias_acima} dias com faturamento acima da média mensal.")

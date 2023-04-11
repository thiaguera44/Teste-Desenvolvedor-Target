# declarando variaveis
sp = 67836.43
rj = 36678.66
mg = 29229.48
es = 27165.48
outros = 19849.53

total = (sp + rj + mg + es + outros)

print(f'O faturamento total da empresa foi de \33[32mR${total:.2f}\33[m')

escolha = (int(input('Qual estado você deseja saber a porcentagem: '
                '\n[1]São Paulo \n[2]Rio de Janeiro \n[3]Minas Gerais'
                '\n[4]Espirito Santo \n[5]Outros \n ----> ')))

if escolha == 1:
    porc = sp / total * 100
    print(f'São Paulo tem {porc:.2f}% do faturamento mensal!')

elif escolha == 2:
    porc = rj / total * 100
    print(f'Rio de Janeiro tem {porc:.2f}% do faturamento mensal!')

elif escolha == 3:
    porc = mg / total * 100
    print(f'Minas Gerais tem {porc:.2f}% do faturamento mensal!')

elif escolha == 4:
    porc = es / total * 100
    print(f'Espirito Santo tem {porc:.2f}% do faturamento mensal!')

elif escolha == 5:
    porc = sp / total * 100
    print(f'Os outros estados tem {porc:.2f}% do faturamento mensal!')

else:
    print('\33[31mERRO, CÓDIGO NÃO ENCONTRADO!\33[m')

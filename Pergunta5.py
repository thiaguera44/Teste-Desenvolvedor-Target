def inverteString(string):
    # Invertendo o string usando o operador de fatiamento [::-1]
    return string[::-1]

# Exemplo de uso
string1 = str(input('Digite qualquer coisa: '))
inverso = inverteString(string1)
print(f'Essa é a sua frase invertida:\n{inverso}')

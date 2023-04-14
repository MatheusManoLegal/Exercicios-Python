# Solicita ao usuário que digite 5 números
print("Digite 5 números:")
numeros = []
for i in range(5):
    numero = float(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

# Calcula a soma dos números
soma = sum(numeros)

# Calcula a média dos números
media = soma / len(numeros)

# Imprime a soma e a média dos números
print("A soma dos números é:", soma)
print("A média dos números é:", media)

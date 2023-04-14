# Solicita ao usuário que digite 5 números
print("Digite 5 números:")
numeros = []
for i in range(5):
    numero = float(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

# Encontra o maior número na lista de números
maior_numero = max(numeros)

# Imprime o maior número
print("O maior número é:", maior_numero)

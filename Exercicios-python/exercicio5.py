# Leitura dos números inteiros
vetor = []
for i in range(20):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(num)

# Separação dos números pares e ímpares
par = []
impar = []
for num in vetor:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

# Impressão dos vetores
print("Números digitados: ", vetor)
print("Números pares: ", par)
print("Números ímpares: ", impar)

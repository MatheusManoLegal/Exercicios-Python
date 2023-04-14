# Solicita ao usuário que digite os dois números inteiros
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Verifica qual é o menor e o maior número
menor = min(numero1, numero2)
maior = max(numero1, numero2)

# Gera e imprime os números inteiros no intervalo compreendido por eles
print("Números inteiros no intervalo entre", menor, "e", maior, ":")
for i in range(menor, maior + 1):
    print(i)

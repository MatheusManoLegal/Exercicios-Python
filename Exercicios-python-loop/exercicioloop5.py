while True:
    try:
        populacao_a = float(input("Informe a população do país A: "))
        taxa_crescimento_a = float(input("Informe a taxa de crescimento anual do país A (em decimal): "))
        populacao_b = float(input("Informe a população do país B: "))
        taxa_crescimento_b = float(input("Informe a taxa de crescimento anual do país B (em decimal): "))
        anos = 0

        while populacao_a < populacao_b:
            populacao_a += populacao_a * taxa_crescimento_a
            populacao_b += populacao_b * taxa_crescimento_b
            anos += 1

        print("Número de anos necessários:", anos)
        resposta = input("Deseja calcular novamente? (s/n): ")
        if resposta.lower() != "s":
            break

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")

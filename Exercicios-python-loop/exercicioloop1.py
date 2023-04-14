while True:
    nota = float(input("Por favor, informe uma nota entre zero e dez: "))
    if nota >= 0 and nota <= 10:
        print("Nota válida:", nota)
        break
    else:
        print("Valor inválido. Por favor, informe uma nota entre zero e dez.")

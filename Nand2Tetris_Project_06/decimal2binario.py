def decimal2binario(numero_decimal):
    numero_binario = 0
    multiplicador = 1

    while numero_decimal != 0:
        # se almacena el módulo en el orden correcto
        numero_binario = numero_binario + numero_decimal % 2 * multiplicador
        numero_decimal //= 2
        multiplicador *= 10

    numero_binario = str(numero_binario)
    while len(numero_binario) < 16:
        numero_binario = "0" + numero_binario

    return numero_binario

def morral(size, pesos, valores, n):
    if n == 0 or size ==0 :
        return 0

    if pesos[n-1] > size:
        return morral(size, pesos, valores, n-1)

    return max(valores[n-1]+morral(size-pesos[n-1], pesos, valores, n-1),
                morral(size, pesos, valores, n-1))



if __name__ == "__main__":
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    size = 50
    n = len(valores)

    resultado = morral(size, pesos, valores, n)
    print(resultado)
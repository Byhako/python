import random

def tirar_dato(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6])
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros


def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dato(numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    tiros_1 = 0
    for tiro in tiros:
        if 1 in tiro:
            tiros_1 += 1

    prob_tiros_1 = tiros_1/numero_de_intentos
    print(f'Probabilidad de obtener por lo menos un 1 en {numero_de_tiros} tiros = {prob_tiros_1}')



if __name__ == "__main__":
    numero_de_tiros = int(input('Cuantas veces lanzamos el dado? '))
    numero_de_intentos = int(input('Cuantas veces corremos la simulación? '))

    main(numero_de_tiros, numero_de_intentos)
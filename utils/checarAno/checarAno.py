
def verSeAnoEBissexto(ano):
    return True if (ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0) else False

def verAnosBissextosProximosAoAnoDigitado(ano):
    anosBissextos = []


    for i in range(ano, -1, -1):
        if (i % 4 == 0 and i % 100 != 0) or (i % 4 == 0 and i % 100 == 0 and i % 400 == 0):
            anosBissextos.append(i)
            break

    anoBissextoPosterior = ano

    while True:
        if (anoBissextoPosterior % 4 == 0 and anoBissextoPosterior % 100 != 0)\
                or (anoBissextoPosterior % 4 == 0 and anoBissextoPosterior % 100 == 0 and anoBissextoPosterior % 400 == 0):
            anosBissextos.append(anoBissextoPosterior)
            break
        anoBissextoPosterior += 1

    return anosBissextos


def verSeAnoEBissexto(ano):
    return True if (ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0) else False
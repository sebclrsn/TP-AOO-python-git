"""
Module pour le traitement des mesures
*************************************
"""
def calculate_moving_average(data: list[float], interval: int):
    moyenne_glissante = 0
    n = 4
    for i in range(n,interval+n):
        moyenne_glissante = moyenne_glissante + list[n-i]
    moyenne_glissante = moyenne_glissante / interval
    return moyenne_glissante
"""
Module pour le traitement des mesures
*************************************
"""

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
interval = 4


def calculate_moving_average(data: list[float], interval: int):
    """Lissage du signal
    param data: liste du signal
    param interval: fenêtre de la moyenne glissante"""

    new_list = []
    for k in range(0, len(data) - interval):
        somme = 0
        for i in range(interval):
            somme += data[k + i]
        new_list.append((1 / interval) * somme)
    return new_list

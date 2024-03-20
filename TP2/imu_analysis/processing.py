"""
Module pour le traitement des mesures
*************************************
"""


def calculate_moving_average(data: list[float], interval: int):
    data_moy = []
    for d in range(0, len(data) - interval):
        moy = 0
        for i in range(interval):
            moy += data[d + i]
        data_moy.append(moy / interval)
    return data_moy


print(calculate_moving_average([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4))

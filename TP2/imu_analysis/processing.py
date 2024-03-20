"""
Module pour le traitement des mesures
*************************************
"""


def calculate_moving_average(data: list[float], interval: int):
    n = 4
    moy_g = 0
    N = len(interval)
    for i in range(n, interval + n):
        moy_g = moy_g + list(n + i)
    moy_g = 1 / N * moy_g
    print(moy_g)
    print("JSP si ça fonctionne ")
    return 0

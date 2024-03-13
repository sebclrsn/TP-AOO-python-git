"""
Module pour le traitement des mesures
*************************************
"""


def calculate_moving_average(data: list[float], interval: int):
    moy_g = 0
    N = len(interval)
    for i in range(0, interval - 1):
        for j in range(N, i + N):
            moy_g = (1 / N) * sum(data[i])
            print(moy_g)
    print("JSP si ça fonctionne ")
    return 0

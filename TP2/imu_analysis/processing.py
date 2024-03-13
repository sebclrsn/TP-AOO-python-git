"""
Module pour le traitement des mesures
*************************************
"""


def calculate_moving_average(data: list[float], interval: int):
    mov_ave = 0
    for i in range(interval):
        mov_ave += data[i]
    mov_ave = mov_ave / interval
    return mov_ave

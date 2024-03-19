"""
Module pour le traitement des mesures
*************************************
"""


def calculate_moving_average(data: list[float], interval: int):
    x_list = []
    for i in range(len(data) - interval + 1):
        slide_average = sum(data[i:interval + i])
        x_list.append(slide_average / interval)
    return x_list

# data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# interval = 4
# print(calculate_moving_average(data, interval))

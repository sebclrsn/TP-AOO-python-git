"""
Module pour le traitement des mesures
*************************************
"""
def calculate_moving_average(data: list[float], interval: int):
    av=[]
    n=len(data)
    for i in range(n-interval):
        s=sum(data[i:i+interval])/interval
        av.append(s)
    return av



data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 4
print(calculate_moving_average(data,n))


